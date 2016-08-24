#1 make_response()
from flak import make_response


@app.route('/')
def index():
	response = make_response('<h1>This document caries a cookie!</h1>')
	response.set_cookie('answer', '42')
	return response
	
#2 redirect()
from flask import redirect


@app.route('/')
def index():
	return redirect('http://www.example.com')
	
#3 abort()
from flask import abort

@app.route('/')
def get_user('/user/<id>')
	user = load_user(id)
	if not user:
		abort(404)
	return '<h1>Hello, %s</h1>' % user.name