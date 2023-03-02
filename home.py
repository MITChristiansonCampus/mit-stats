from flask import Flask
from flask import render_template, request

import pygsheets

app = Flask(__name__)

@app.route("/")
def home():
    return "MIT Stats Slack App"

@app.route("/appt", methods=['post', 'get'])
def appt():
    print (request.get_json())
    return "testing"