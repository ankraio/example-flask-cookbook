FROM registry.infra.ankra.cloud/alpine/python3:11

# Application Setup
COPY src/requirements.txt /opt/src/requirements.txt
RUN pip3 install -r /opt/src/requirements.txt
COPY src /opt/src

RUN apk add --no-cache openssl tini

ADD entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
