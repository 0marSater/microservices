from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_service_one():
    return 'Hello from Service One!'


@app.route('/test')
def test():
    return 'test'


if __name__ == '__main__':
    app.run(port=5001, debug=True)
