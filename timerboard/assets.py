from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask.ext.assets import Bundle, Environment

assets = Environment()
assets.from_yaml("timerboard/static/vendor.yaml")
assets.from_yaml("timerboard/static/custom.yaml")

mod = Blueprint('assets', __name__, template_folder='templates')

@mod.route("/fonts/<path:filename>")
def fonts(filename):
	return redirect(url_for('static', filename="bower_components/font-awesome/fonts/"+filename))
