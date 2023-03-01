from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "MIT Stats Slack App"

@app.route("/appt", methods=['post', 'get'])
def appt():
    print (request)