FROM python:3.9.6-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5005

ENV FLASK_APP=app.py

CMD ["flask", "run", "--port", "5005", "--host=0.0.0.0"]