FROM balenalib/raspberry-pi-debian-python:latest

MAINTAINER Sean Connolly <connolly.st@gmail.com>

# Install dependencies
RUN apt-get update && apt-get install -y \
    git-core \
    build-essential \
    gcc \
    python \
    python-dev \
    python-pip \
    python-virtualenv \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY main.py /
COPY PCA9685.py /

CMD [ "python", "./main.py" ]