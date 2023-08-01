#!/usr/bin/env python3
"""
i18n exercises
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ Babel i18n configuration """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route("/")
def hello() -> str:
    """ Base route for application """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
