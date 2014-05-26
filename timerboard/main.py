from flask import Flask, render_template, send_from_directory, url_for, redirect
from flask.ext.assets import Environment, Bundle
from flask.ext.login import LoginManager
from timerboard.assets import assets
import os

login_manager = LoginManager()


@login_manager.user_loader
def load_user(userid):
	return {}

def create_app():   # We could pass a config object here
    app = Flask(__name__)

    # Register template filters here
    # app.add_template_filter(some_method)

    #app.config.from_object(config)
    #app.config.from_pyfile(config_filename)

    app.secret_key = os.urandom(24)
    assets.init_app(app)
    login_manager.init_app(app)

    from timerboard.database import db
    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app
