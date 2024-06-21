#!/usr/bin/env python3
""" Starts a Flash Web Application """
from flask import Flask, render_template, g, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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


def get_user(id):
    if id in users:
        return users[id]
    return None


@app.before_request
def before_request():
    values_dict = dict_maker()
    user_dict = {}
    if 'login_as' in values_dict:
        user_dict = get_user(int(values_dict['login_as']))
        if user_dict is not None:
            g.user = user_dict

@app.route('/', strict_slashes=False)
def main_page():
    """Just prints a simple messages"""
    return render_template('5-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
