# FROM python:3.8.19-alpine
# FROM python:3.10.14-alpine
FROM python:3.11.9-alpine
# FROM python:3.12.5-alpine # Not working Kafka issue

# Set environment variables for paths and configurations
ENV WORKDIR_PATH=/home/fastapi-template

WORKDIR $WORKDIR_PATH
COPY src/requirements.txt $WORKDIR_PATH

# Install the required Python packages. You can remove --no-cache-dir if you are okay with cache.
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt

COPY src $WORKDIR_PATH

# Command to run the FastAPI app using Uvicorn with the custom logging configuration
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8081", "--workers", "1", "--timeout-keep-alive", "1000"]
