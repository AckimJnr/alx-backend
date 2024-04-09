#!/usr/bin/env python3
"""2nd app module"""
from flask import request
from flask_babel import Babel


class Config:
    """
    Contain language configurations
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAUL_TIMEZONE = "UTC"


app = Flask(__name__)

app.config.from_object(Config)

babel = Babel(app)
