#!/usr/bin/env python3
from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        fname = secure_filename(f.filename)
        f.save(fname)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)