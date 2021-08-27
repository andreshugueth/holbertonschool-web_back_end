#!/usr/bin/env python3
""" 1-app module """
from flask import Flask, request
from flask_babel import Babel
from routes.routes_2 import app_routes


app = Flask(__name__)
babel = Babel(app)

app.config.from_object('1-app.Config')
app.register_blueprint(app_routes)


@babel.localeselector
def get_locale() -> str:
    """ Determine best match for supported languages
    """
    return request.accept_languages.best_match(['en', 'fr'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
