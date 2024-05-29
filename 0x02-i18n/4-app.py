#!/usr/bin/env python3
"""module to create flask app instance"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """class to set the configuration for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """return the best matched language from request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """renders template with hello hbnb"""
    locale_arg = request.args.get('locale', '')
    if locale_arg and locale_arg in Config.LANGUAGES:
        return locale_arg
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()
