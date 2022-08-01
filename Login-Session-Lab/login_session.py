from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/', methods=['POST', 'GET'] ) # What methods are needed?
def home():
	if request.method == "GET":
		return render_template('home.html')
	else:
		try:
			login_session['name'] = request.form['name']
			login_session['age'] = request.form['age']
			login_session['qoute'] = request.form['qoute']

			return redirect(url_for('thanks'))
		except:
			return redirect(url_for('error'))

	


@app.route('/error')
def error():

	return render_template('error.html')



@app.route('/display')
def display():

	return render_template('display.html', name=login_session['name'], age = login_session['age'], qoute = login_session['qoute']) # What variables are needed?



@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)