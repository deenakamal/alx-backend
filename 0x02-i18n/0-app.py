#!/usr/bin/env python3
""" 0-app  Module"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index() -> str:
    """Returns a string as a response"""
    return render_template("0-index.html")
