FROM python:3.12-alpine
WORKDIR /app/
#instala recursos para comunicação com o postgres
RUN apk update && apk add --no-cache \
    libpq-dev \
    build-base


COPY ./requeriments.txt ./requeriments.txt

RUN pip install --no-cache-dir -r requeriments.txt
COPY . .
CMD [ "uvicorn", "api.main:app", "--reload", "--host", "0.0.0.0"]