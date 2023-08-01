#!/usr/bin/env python3
"""
i18n exercises
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello():
    """ Base route for application """
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
