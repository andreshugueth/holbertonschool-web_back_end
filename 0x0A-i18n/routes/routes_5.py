#!/usr/bin/env python3
"""Basic route task 5"""
from typing import Union
from flask import Blueprint, render_template, request, g


app_routes = Blueprint('app_routes', __name__)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[dict, None]:
    """get user"""
    try:
        return users.get(int(request.args.get('login_as')))
    except Exception:
        return None


@app_routes.route('/', methods=["GET"], strict_slashes=False)
def home():
    """ Home page """
    return render_template('5-index.html')


@app_routes.before_request
def before_request():
    """ before request
    """
    g.user = get_user()
