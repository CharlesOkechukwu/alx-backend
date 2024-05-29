#!/usr/bin/env python3
"""module to create flask app instance"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """renders template with hello hbnb"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()