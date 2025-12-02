from flask import Flask

app = Flask(__name__)      //creating flask app instance

@app.route('/')             //decorate(if someone is trying to talk with API is the user is authenticated or not)
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run("0.0.0.0")
