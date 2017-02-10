from flask import Flask

app = Flask(__name__)
@app.route("/")
def welcome():
    return "Welcome to test service"

@app.route("/test1")
def test1():
    return "Test #1"


@app.route("/test2")
def test2():
    return "Test #2"

@app.route("/test3")
def test3():
    return "Test #3"

@app.route("/test4")
def test4():
    return "Test #4"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
