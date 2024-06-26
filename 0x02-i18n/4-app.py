#!/usr/bin/env python3
""" Starts a Flash Web Application """
from flask import Flask, render_template, g, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Here you can find the configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def dict_maker():
    queries = request.query_string.decode('utf-8').split('&')
    values_dict = {}
    elm_list = []
    if len(queries[0]) != 0:
        for elm in queries:
            elm_list = elm.split('=')
            values_dict[elm_list[0]] = elm_list[1]
    return values_dict

@babel.localeselector
def get_locale():
    """A locator function"""
    values_dict = dict_maker()
    for key, value in values_dict.items():
        if key == 'locale' and value in Config.LANGUAGES:
            return value
        else:
            return request.accept_languages.best_match(Config.LANGUAGES)
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/', strict_slashes=False)
def main_page():
    """Just prints a simple messages"""
    return render_template('4-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
