
FROM alpine:latest

ADD requirements.txt requirements.txt

RUN apk add --update \
    python \
    python-dev \
    py-pip \
    openssl-dev \
    libffi-dev \
    musl-dev \
    gcc \
    g++ \
    py-numpy \
    py-numpy-dev \
    ca-certificates \
    linux-headers \
    make \
    su-exec \
    shadow \
    bash

RUN pip install -U pip && pip install -r requirements.txt

ADD docker/entry.sh entry.sh
ADD docker/main.sh main.sh
VOLUME /data
WORKDIR /data
ENTRYPOINT ["/entry.sh"]
