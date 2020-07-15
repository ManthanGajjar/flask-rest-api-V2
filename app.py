from flask import Flask

app = Flask(__name__)

@app.route('/')
def initialRoute():
    return 'Hello, Welcome to Flask API demo'

if (__name__ == '__main__'):
    app.run()