FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY Dns-To-DnsOverTls-Proxy.py .

EXPOSE 12853

CMD ["python", "Dns-To-DnsOverTls-Proxy.py"]
