from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_service_two():
    return 'Hello from Service Two!'


if __name__ == '__main__':
    app.run(port=5002)
