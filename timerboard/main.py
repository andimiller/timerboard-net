from flask import Flask, render_template
from flask.ext.assets import Environment, Bundle
from timerboard.assets import assets

app = Flask(__name__)
assets.init_app(app)

@app.route("/")
def index():
	print "hi"
	return render_template("index.html")

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8090, debug=True)
