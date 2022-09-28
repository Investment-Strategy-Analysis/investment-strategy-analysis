FROM python:3.9-slim-buster

WORKDIR /app

RUN apt-get update
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . services/user_service/

CMD ["uvicorn" , "services.user_service.api.api:app" , "--host", "0.0.0.0", "--port", "8000"]
