FROM python:3.10-slim
RUN apt-get update && apt-get install -y nmap tcpdump && rm -rf /var/lib/apt/lists/*
RUN pip install pymodbus==3.6.9
WORKDIR /app
CMD ["tail", "-f", "/dev/null"]
