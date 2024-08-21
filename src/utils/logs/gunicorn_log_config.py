import logging
import logging.config
import sys
from pyconman import ConfigLoader

# Load configuration and get the service name
config = ConfigLoader.get_config()
service_name = config.get("service", "default-service")

gunicorn_log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "generic": {
            "format": f"%(asctime)s [server] [-] [{service_name}] [%(levelname)-4s] [%(filename)s:%(lineno)d] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "access": {
            "format": "%(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "generic",
            "stream": sys.stdout,
        },
        "error_file": {
            "class": "logging.FileHandler",
            "formatter": "generic",
            "filename": "/tmp/gunicorn.error.log",
        },
        "access_file": {
            "class": "logging.FileHandler",
            "formatter": "access",
            "filename": "/tmp/gunicorn.access.log",
        },
    },
    "loggers": {
        "gunicorn.error": {
            "level": "INFO",
            "handlers": ["error_file"],
            "propagate": True,
        },
        "gunicorn.access": {
            "level": "INFO",
            "handlers": ["access_file"],
            "propagate": False,
        },
        "root": {
            "level": "INFO",
            "handlers": ["console"],
        },
    },
}

# Apply the logging configuration
logging.config.dictConfig(gunicorn_log_config)