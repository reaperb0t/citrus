#!/usr/bin/python

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
    #processed_text = text.upper()
    #print(processed_text)
    print(text)
    return redirect('/')

if __name__ == '__main__':
    app.run()
