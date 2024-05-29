#!/usr/bin/env python3
"""module to create flask app instance"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config(object):
    """class to set the configuration for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """get user from request"""
    id = request.args.get('login_as')
    if id:
        return users.get(int(id))
    return None


@app.before_request
def before_request():
    """perform actions before each request"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """return the best matched language from request"""
    locale_arg = request.args.get('locale', '').strip()
    if locale_arg and locale_arg in Config.LANGUAGES:
        return locale_arg
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """renders template with hello hbnb"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run()
