FROM python:3.11-bookworm

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]