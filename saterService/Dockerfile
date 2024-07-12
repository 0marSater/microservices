FROM python:3.10-alpine

WORKDIR /app

COPY reqs.txt /app

RUN pip install --no-cache-dir -r reqs.txt

COPY . /app

EXPOSE 5001

CMD ["python", "main.py"]