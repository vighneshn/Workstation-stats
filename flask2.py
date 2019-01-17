#!/usr/bin/env python
from flask import Flask, request, redirect, render_template, url_for
import subprocess
import re
app = Flask(__name__)

@app.route('/', methods=['GET','POST']) 
def hello_world():
	if request.method == 'POST':
		if 'df' in request.form:
			return redirect(url_for('df'))
		if 'top' in request.form:
			return redirect('/top')		
		if 'nvidia-smi' in request.form:
			return redirect('/nvidia-smi')		
	return render_template('buttons.html')

@app.route('/df') 
def df():
	out = subprocess.Popen(['df','-h'],
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
	result, err = out.communicate()
	result = '<pre>'+result+'</pre>'
	return result

@app.route('/top') 
def top():
        out = subprocess.Popen(['top','-l','1'],
           stdout=subprocess.PIPE,
           stderr=subprocess.STDOUT)
        result, err = out.communicate()
	result = '<pre>'+result+'</pre>'
	return result
	
@app.route('/nvidia-smi') 
def nvidia():
        out = subprocess.Popen(['nvidia-smi'],
           stdout=subprocess.PIPE,
           stderr=subprocess.STDOUT)
        result, err = out.communicate()
	result = '<pre>'+result+'</pre>'
	return result

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
