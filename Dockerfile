FROM python:latest
ADD database.config /database.config
ADD requirements.txt /requirements.txt
ADD app /app
RUN pip install -r requirements.txt
CMD ["python", "/app/main.py"]
