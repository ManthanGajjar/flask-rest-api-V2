from flask import Flask
import os

app = Flask(__name__)
# set .env file to perform this operations
# app.config.from_object(os.environ['APP_SETTINGS'])
@app.route('/')
def initialRoute():
    return 'Hello, Welcome to Flask API demo'

# call hello <route name>
@app.route('/me/<name>')
def callMyName(name):
    return 'Hello ' + name 

if (__name__ == '__main__'):
    app.run()