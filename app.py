#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# file: app.py

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/request")
def request_info():
	return f"request method: {request.method} url: {request.url} headers: {request.headers}"

@app.route("/")
def hello():
	return "Hello"

if __name__ == "__main__":
	app.run(debug=True)