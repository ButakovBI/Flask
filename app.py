from flask import Flask

app = Flask(__name__)


@app.route('/')
def test():
    return 'Hello, World!'


@app.route('/about/<name>')
def about(name: str):
    return f"It's me, {name}"


@app.route('/<expression>/')
def f(expression):
    return str(eval(expression.replace(":", "/")))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
