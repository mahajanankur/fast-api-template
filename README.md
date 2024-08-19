# Python FastAPI REST Web Service Template

This repository provides a template for creating a Python FastAPI REST web service. It is designed to be suitable for both novice and experienced programmers.

## Getting Started
Clone the repository onto your local machine.

### Install the necessary dependencies.
```bash
pip install -r requirements.txt
```
### Run the FastAPI web service by Python3.
```bash
python3 src/app.py
```
### Run the FastAPI web service by Docker.
This will run a production level **[Gunicorn](https://gunicorn.org/#quickstart)** server.
```bash
docker-compose up --build
```
## Usage
To use the web service, send HTTP requests to the appropriate endpoint using a tool such as cURL or Postman. The endpoints that are currently available are:

**/health** - Health check of the service.

**/api/products** - Returns a JSON array of all the products.

## Contributing
If you find a bug or would like to suggest an improvement, please open an issue or create a pull request. All contributions are welcome!

---
License
----
**Apache 2.0**

**Free Software, Hell Yeah!**