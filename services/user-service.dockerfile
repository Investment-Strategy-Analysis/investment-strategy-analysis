FROM python:3.9-slim-buster

WORKDIR /app

RUN apt-get update
COPY user_service/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY user_service/ services/user_service/
COPY common/ services/common/

CMD ["uvicorn" , "services.user_service.api.api:app" , "--host", "0.0.0.0", "--port", "8000", "--reload"]
