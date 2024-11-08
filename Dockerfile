FROM python:3.12-alpine
WORKDIR /app

COPY ./requeriments.txt ./requeriments.txt

RUN pip install --no-cache-dir -r requeriments.txt
COPY . .
CMD [ "python3", "./api/main.py"]