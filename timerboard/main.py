from flask import Flask, render_template, send_from_directory, url_for, redirect
from flask.ext.assets import Environment, Bundle
from flask.ext.login import LoginManager
from timerboard.assets import assets

app = Flask(__name__)
assets.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
	return {}

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/fonts/<path:filename>")
def fonts(filename):
	return redirect(url_for('static', filename="bower_components/font-awesome/fonts/"+filename))

import os
app.secret_key = os.urandom(24)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8090, debug=True)
