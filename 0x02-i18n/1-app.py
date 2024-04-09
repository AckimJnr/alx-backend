#!/usr/bin/env python3
"""2nd app module"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Contain language configurations
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)

app.config.from_object(Config)

babel = Babel(app)


@app.route("/")
def index() -> str:
    """
    Root route of our application
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    """
    If main module execute
    """
    app.run(host='0.0.0.0', port='5000')
