#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)

class Config:
    """Here you can find the configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

@app.route('/', strict_slashes=False)
def main_page():
    """Just prints a simple messages"""
    return render_template('0-index.html')

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
