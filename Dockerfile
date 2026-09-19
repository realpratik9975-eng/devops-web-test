FROM python:3.12

WORKDIR /app

COPY metrics_server.py .

EXPOSE 8000

CMD ["python3", "metrics_server.py"]
