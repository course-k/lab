'''
Created on 2022/05/21

@author: Kousuke
'''

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def render_form():
	return render_template('index.html')


@app.route('/', methods=['POST'])
def login():
	if request.form['username'] and request.form['email']:
		return render_template('check.html', email=request.form['email'], username=request.form['username'])
	else:
		return render_template('error.html')


if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)
