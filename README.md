# Python FastAPI REST Web Service Template

This repository provides a comprehensive template for creating a Python-based FastAPI REST web service. It is designed to help both novice and experienced developers quickly set up a robust, production-ready web service.

## Table of Contents
1. [Getting Started](#getting-started)
2. [Installation](#installation)
3. [Running the Service](#running-the-service)
   - [Locally with Python](#run-locally-with-python)
   - [Using Docker](#run-using-docker)
4. [Endpoints](#endpoints)
5. [Logging Configuration](#logging-configuration)
6. [Contributing](#contributing)
7. [License](#license)

## Getting Started

Clone the repository onto your local machine:
```bash
git clone https://github.com/mahajanankur/fast-api-template.git
cd fastapi-web-service-template
```

## Installation

### Install Dependencies

Ensure you have Python 3.8+ installed. Then, install the required Python packages:
```bash
pip install -r requirements.txt
```

## Running the Service

### Run Locally with Python

To run the FastAPI web service locally using Python:
```bash
python3 src/app.py
```

This will start the FastAPI server on `http://localhost:8081`.

### Run Using Docker

To run the FastAPI web service in a Docker container with production-level settings (using **[Gunicorn](https://gunicorn.org/#quickstart)** and Uvicorn):
```bash
docker-compose up --build
```

This will start the service in a Docker container, accessible on `http://localhost:8081`.

## Endpoints

### Health Check

**GET /health**  
- **Description**: Simple health check endpoint to verify that the service is running.
- **Response**: `{"status": "healthy"}`

### Products API

**GET /api/products**  
- **Description**: Returns a JSON array of all the products.
- **Response**: A list of products in JSON format.

### Custom Endpoints

You can add more endpoints to `src/resources` and define their corresponding logic in the service layers. Follow the existing structure for consistency.

## Logging Configuration

This template uses a custom logging configuration designed for production environments. Logs are categorized into error logs and access logs, with flexibility for customization. The logging configuration is defined in the `uvicorn_log_config.py` file.

### Dynamic Service Name in Logs

The log format dynamically includes the service name from your configuration:
```python
service_name = config.get("service", "default-service")
```

You can modify the logging configuration in `uvicorn_log_config.py` to fit your needs.

## Contributing

We welcome contributions to enhance this template. If you find a bug or have suggestions for improvements, please open an issue or submit a pull request. Contributions are greatly appreciated!

### How to Contribute

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a pull request.

## License

This project is licensed under the **Apache 2.0** License. See the `LICENSE` file for more details.
