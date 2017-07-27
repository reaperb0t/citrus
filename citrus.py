#!/usr/bin/python

#@reaperb0t
#IST 885 Penn State University
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def citrus():
    return render_template("citrus.html")

@app.route('/', methods=['POST'])
def citrus_post():
    text = request.form['text']
    print(text)
    return redirect('/')

if __name__ == '__main__':
    app.run()
