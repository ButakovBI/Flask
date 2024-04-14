from flask import Flask

app = Flask("My project")


@app.route('/')
def test():
    return 'Hello, World!'


@app.route('/about')
def about():
    return "It's me, Bogdan"


if __name__ == '__main__':
    app.run(debug=True)

