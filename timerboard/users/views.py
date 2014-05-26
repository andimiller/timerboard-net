from flask import Blueprint, render_template, g

mod = Blueprint('users', __name__, template_folder='templates')


@mod.route("/")
def index():
    return render_template("index_guest.html")
