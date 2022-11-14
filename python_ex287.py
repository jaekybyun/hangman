#[python_ex287.py]
#http://tinyurl.com/h59sdyu

from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
	return "Hello, Jaeky!"

app.run(port='8000')