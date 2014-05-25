from flask.ext.assets import Bundle, Environment

js = Bundle(
		'bower_components/jquery/dist/jquery.min.js',
		filters='jsmin',
		output='all.js'
		)

assets = Environment()

assets.register('js_all', js)
