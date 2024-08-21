import logging
from pyconman import ConfigLoader
from typing import List, Tuple
from kafka import KafkaConsumer
from concurrent.futures import ThreadPoolExecutor
from .consumer_factory import KafkaConsumerFactory
from .base_processor import BaseMessageProcessor

# Load configuration and initialize logging
config = ConfigLoader.get_config()
logger = logging.getLogger(config.get("service"))

class KafkaConsumerRunner:
    def __init__(self, consumer_factory: KafkaConsumerFactory, topics: List[Tuple[str, BaseMessageProcessor]], max_workers: int, server):
        self.consumer_factory = consumer_factory
        self.topics = topics
        self.max_workers = max_workers
        self.consumers = {}
        self.server = server
        logger.info(f"KafkaConsumerRunner initialized with {len(topics)} topics and {max_workers} workers.")

    def start_consumers(self):
        """
        Start Kafka consumers for each topic.
        """
        logger.info("Starting Kafka consumers...")
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            for topic, message_processor in self.topics:
                try:
                    consumer, processor = self.consumer_factory.create_consumer(topic, message_processor)
                    self.consumers[topic] = consumer
                    logger.info(f"Consumer created for topic: {topic}")
                    executor.submit(self._start_consumer, consumer, processor)
                except Exception as e:
                    logger.error(f"Error creating consumer for topic {topic}: {str(e)}")

    def stop_consumers(self):
        """
        Stop all Kafka consumers.
        """
        logger.info("Stopping all Kafka consumers...")
        for topic, consumer in self.consumers.items():
            try:
                consumer.close()
                logger.info(f"Consumer for topic {topic} stopped.")
            except Exception as e:
                logger.error(f"Error stopping consumer for topic {topic}: {str(e)}")

    def _start_consumer(self, consumer: KafkaConsumer, message_processor: BaseMessageProcessor):
        """
        Start a Kafka consumer and process messages.
        """
        logger.info(f"Starting consumer for topic: {consumer.subscription()}")
        with self.server.app_context():
            try:
                for message in consumer:
                    try:
                        logger.debug(f"Received message from topic {message.topic}: {message.value}")
                        message_processor.process_message(message.value)
                        logger.debug(f"Message processed successfully for topic {message.topic}")
                    except Exception as e:
                        logger.error(f"Error processing message from topic {message.topic}: {str(e)}")
            except Exception as e:
                logger.error(f"Exception occurred while consuming messages: {str(e)}")
