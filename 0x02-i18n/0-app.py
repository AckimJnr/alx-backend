#!/usr/bin/env python3
"""app module"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index() -> str:
    """
    Root route of our application
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    """
    If main module execute
    """
    app.run(host='0.0.0.0', port='5000')
