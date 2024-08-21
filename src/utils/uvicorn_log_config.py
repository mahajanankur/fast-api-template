import logging
import sys
from pyconman import ConfigLoader
config = ConfigLoader.get_config()
service_name = config.get("service")

log_config = {
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
            "filename": "/tmp/uvicorn.error.log",
        },
        "access_file": {
            "class": "logging.FileHandler",
            "formatter": "access",
            "filename": "/tmp/uvicorn.access.log",
        },
    },
    "loggers": {
        "uvicorn": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False,
        },
        "uvicorn.error": {
            "level": "INFO",
            "handlers": ["error_file"],
            "propagate": True,
        },
        "uvicorn.access": {
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

if __name__ == "__main__":
    logging.config.dictConfig(log_config)
