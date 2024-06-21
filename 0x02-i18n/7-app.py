#!/usr/bin/env python3
""" Starts a Flash Web Application """
from flask import Flask, render_template, g, request
from flask_babel import Babel
import pytz


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
    """What is this function btw?"""
    queries = request.query_string.decode('utf-8').split('&')
    values_dict = {}
    elm_list = []
    if len(queries[0]) != 0:
        for elm in queries:
            elm_list = elm.split('=')
            values_dict[elm_list[0]] = elm_list[1]
    return values_dict


@babel.timezoneselector
def get_timezone():
    """A locator function but this time it's for time"""
    values_dict_query = dict_maker()
    timezone = ''
    for key, value in values_dict_query.items():
        if key == 'timezone':
            timezone = value
    if g.user:
        timezone = g.user['timezone']
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@babel.localeselector
def get_locale():
    """A locator function"""
    values_dict_query = dict_maker()
    for key, value in values_dict_query.items():
        if key == 'locale' and value in Config.LANGUAGES:
            return value
    if g.user and g.user['locale'] in Config.LANGUAGES:
        return g.user['locale']
    header_locale = request.headers.get('locale', '')
    if header_locale in Config.LANGUAGES:
        return header_locale
    return request.accept_languages.best_match(Config.LANGUAGES)


def get_user(id):
    """I think this function can get users"""
    if id in users:
        return users[id]
    return None


@app.before_request
def before_request():
    """Why are you asking?"""
    values_dict = dict_maker()
    user_dict = {}
    condition = 0
    if 'login_as' in values_dict:
        user_dict = get_user(int(values_dict['login_as']))
        if user_dict is not None:
            g.user = user_dict
            condition = 1
    if (condition == 0):
        g.user = None


@app.route('/', strict_slashes=False)
def main_page():
    """Just prints a simple messages"""
    return render_template('6-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
