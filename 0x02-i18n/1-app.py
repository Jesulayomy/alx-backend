#!/usr/bin/env python3
""" This module is for a simple flask appth Babel """
from flask import (
    Flask,
    render_template,
)
from flask_babel import Babel
from typing import Any


class Config(object):
    """ Configuration class for babel presets """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route('/', strict_slashes=False)
def home() -> Any:
    """ Home page of the application """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
