from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def principal():
    return render_template('home.html')


@app.route("/about")
def principal():
    return 'about'


if __name__ == '__main__':
    app.run()
