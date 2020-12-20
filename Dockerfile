FROM python:3.7-slim
# FROM cough-recognition:base

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt


CMD [ "python", "/app/api.py" ]