#!/usr/bin/env python3
""" Module"""
from flask import Flask, render_template
from flask_babel import Babel
from flask import request


class Config(object):
    """Configration class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get locale language from request"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index() -> str:
    """Returns a string as a response"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()
