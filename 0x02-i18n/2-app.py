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


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ Detemines the best match with supported languages """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def hello() -> str:
    """ Base route for application """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run()
