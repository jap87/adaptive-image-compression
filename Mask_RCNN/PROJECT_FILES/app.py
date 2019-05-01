import os
import sys
import numpy as np
import skimage.io
from flask import Flask, flash, request, jsonify, url_for, render_template
from werkzeug.utils import secure_filename
import time
import detector

ROOT_DIR = os.path.abspath("../")
UPLOAD_FOLDER = '/images/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/api/compress', methods=['POST'])
def compress():
    if 'file' not in request.files:
        return 'error here'
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        return 'no file'
    if file:
        filename = secure_filename(file.filename)
        print(filename)
        file.save(os.path.join(ROOT_DIR + '/PROJECT_FILES/', filename))
        mask = detector.getMask(filename)
        # os.remove('images/' + filename)
        # Run detection
        response_body = 'hello'
        return response_body
    return 'error at file level'

@app.route('/')
def index():
    return render_template('index.html')
