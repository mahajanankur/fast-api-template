import logging
import threading
import time, json
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from motifer import FastApiLogFactory 
from models.response import Response
from resources.admin import admin_router
# Kafka consumers
from utils.kafka.consumer_factory import KafkaConsumerFactory
from utils.kafka.runner import KafkaConsumerRunner
from utils.kafka.processor1 import Topic1Processor
from utils.kafka.processor2 import Topic2Processor
from utils.kafka.processor3 import Topic3Processor
from pyconman import ConfigLoader

# Load the configuration in the application scope.
config = ConfigLoader.get_config()

app = FastAPI()

# Initialize logging using FastApiLogFactory
factory = FastApiLogFactory(service=config.get("service"), log_level=logging.DEBUG, server=app)
logger = factory.initialize()

# Register all the routes (assuming admin_router is a FastAPI APIRouter).
app.include_router(admin_router, prefix='/api')

json_config = json.dumps(config)
logger.info(f"Final config JSON = {json_config}")

@app.get('/health')
async def health():
    logger.debug("FastAPI app is running.")
    resp = Response(True, "FastAPI app is running!", None)
    return JSONResponse(content=resp.to_dict())

def init():
    # Initialize all the consumers
    logger.info("Initialize all the consumers.")
    kafka_bootstrap_servers = config["kafka"]["uri"]
    kafka_group_id = "fastapi-group"
    kafka_consumer_factory = KafkaConsumerFactory(kafka_bootstrap_servers, kafka_group_id)

    topics = [
        (config["kafka"]["topics"]["pubsub1"]["name"], Topic1Processor()),
        (config["kafka"]["topics"]["pubsub2"]["name"], Topic2Processor()),
        (config["kafka"]["topics"]["pubsub3"]["name"], Topic3Processor())
    ]

    consumer_runner = KafkaConsumerRunner(
        kafka_consumer_factory, topics, max_workers=len(topics), server=app
    )

    consumer_thread = threading.Thread(
        target=consumer_runner.start_consumers, name=config["kafka"]["thread_group"]
    )
    consumer_thread.start()
    logger.info("Consumers were initialized successfully.")

if config["kafka"]["enabled"]:
    init()

# Main section will not be called in production (e.g., Gunicorn or Uvicorn is recommended).
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8081)
