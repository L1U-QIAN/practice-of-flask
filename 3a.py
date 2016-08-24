from flak import make_response


@app.route('/')
def index():
	response = make_response('<h1>This document caries a cookie!</h1>')
	response.set_cookie('answer', '42')
	return response