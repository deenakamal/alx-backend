#!/usr/bin/env python3
"""Module"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _


class Config:
    """Configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """ Get user """
    try:
        return users.get(int(request.args.get('login_as')))
    except Exception:
        return None


@app.before_request
def before_request():
    """ Before request """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Get the locale Languages"""
    param = request.args.get("locale")
    if param in app.config["LANGUAGES"]:
        return param
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Render 3-index template """
    username = g.user.get("name") if g.user else None
    return render_template('5-index.html', username=username)


if __name__ == "__main__":
    app.run()
