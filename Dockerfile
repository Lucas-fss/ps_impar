FROM python:3.12-alpine
WORKDIR /app/

COPY ./requeriments.txt ./requeriments.txt

RUN pip install --no-cache-dir -r requeriments.txt
COPY . .
CMD [ "uvicorn", "api.main:app", "--reload", "--host", "0.0.0.0"]