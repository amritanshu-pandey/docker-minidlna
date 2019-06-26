FROM alpine:latest
LABEL maintainer="Amritanshu Pandey <amp.msit@gmail.com>"

ADD entrypoint.py /entrypoint.py

RUN apk --no-cache add minidlna bash python3
RUN python3 --version
ENTRYPOINT ["python3", "/entrypoint.py"]

