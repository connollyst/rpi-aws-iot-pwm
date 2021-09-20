FROM balenalib/raspberry-pi-debian:buster-build-20210912

MAINTAINER Sean Connolly <connolly.st@gmail.com>

RUN sudo apt-get update && \
    sudo apt-get install -y \
    python3-pip \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /
RUN python3 -m pip install -r requirements.txt

COPY main.py /
COPY PCA9685.py /
COPY AwsIotCore.py /
COPY certs/ /certs/
CMD [ "python3", "./main.py" ]