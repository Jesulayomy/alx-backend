#!/usr/bin/env python3
""" basic babel methods setup """
from flask import (
    Flask,
    g,
    render_template,
    request,
)
from flask_babel import (
    Babel,
    gettext,
)
from typing import Any


class Config(object):
    """ config classes for babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


def get_locale() -> Any:
    """ get local language request """
    lang = request.args.get('locale')
    if lang and lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Any:
    """ get a user """
    user_id = request.args.get('login_as')
    try:
        return users.get(int(user_id))
    except Exception:
        return None


@app.before_request
def before_request() -> Any:
    """ before request """
    g.user = get_user()


@app.route('/')
def index() -> Any:
    """ render template html """
    if g.user:
        p_text = gettext('logged_in_as', username=g.user.get('name'))
    else:
        p_text = gettext('not_logged_in')

    return render_template('5-index.html',
                           title=gettext('home_title'),
                           body=gettext('home_header'),
                           p_text=p_text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")