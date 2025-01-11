FROM python:3.12-slim
WORKDIR /app
COPY run.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python", "run.py"]
