FROM python:3.8
WORKDIR /home/fastapi-template
# WORKDIR /src
COPY src/requirements.txt /home/fastapi-template
RUN pip install -r requirements.txt
COPY src /home/fastapi-template