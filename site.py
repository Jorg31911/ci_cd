from flask import Flask

app = Flask(__name__)


@app.route("/")
def principal():
    return "<h1> prueba 1 </h1><button>clear<button>"


if __name__ == '__main__':
    app.run()
