from flask.ext.assets import Bundle, Environment

assets = Environment()
assets.from_yaml("timerboard/static/vendor.yaml")
assets.from_yaml("timerboard/static/custom.yaml")
