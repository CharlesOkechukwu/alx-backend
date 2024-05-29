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
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run()
