FROM python:3.10-slim
RUN apt-get update && apt-get install -y iptables iproute2 procps && rm -rf /var/lib/apt/lists/*
RUN pip install pymodbus==3.6.9 flask==3.0.0
WORKDIR /app
COPY . /app
RUN chmod +x /app/start.sh
CMD ["/app/start.sh"]
