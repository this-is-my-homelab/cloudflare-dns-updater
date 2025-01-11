FROM python:3.12-slim
WORKDIR /app
COPY run.py .
RUN pip install requests
CMD ["python", "run.py"]
