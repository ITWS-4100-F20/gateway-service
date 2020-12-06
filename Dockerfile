FROM python:3-alpine

RUN apk update && apk upgrade
RUN apk add gcc musl-dev libffi-dev openssl-dev

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 3030

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]