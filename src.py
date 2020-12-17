from flask import Flask, render_template, Response, request, jsonify, url_for

from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return(render_template("index.html"))