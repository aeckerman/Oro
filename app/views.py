from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'blubrackets'} #N:A('non-active') user
	posts = [
		{
			'author': {'nickname': 'John'},
			'header': 'Started using flask!!!',
			'body': 'Web dev in Python is the best!'
		},
		{
			'author': {'nickname': 'Susan'},
			'header': 'Mozilla Firefox DEV Edition is awesome!!!<3',
			'body': 'Lots of resources...'
		}
	]
	return render_template(
		'index.html',
		title='Home',
		user=user,
		posts=posts
	)