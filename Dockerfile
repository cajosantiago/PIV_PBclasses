FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir \
        numpy \
        scipy \
        opencv-contrib-python-headless

VOLUME ["/app/output"]

ENTRYPOINT ["python", "main.py"]
