from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return

@app.route("/about")
def aabout():
    return "<h1>Про Flask</h1>"

@app.route("/catalog")
def aabout():
    return '<h1 style="text-size: 40px">К сожалению, на данный момент каталог пуст. Приходите чуть позже)</h1>'

if __name__ == "__main__":
    app.run(debug=True)