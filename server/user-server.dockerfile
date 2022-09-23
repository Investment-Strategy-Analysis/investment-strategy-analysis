FROM python:3.9-slim-buster

WORKDIR /app

RUN apt-get update
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . server/

CMD ["uvicorn" , "server.api.api:app" , "--host", "0.0.0.0", "--port", "8000"]
