import os
import sys
import numpy as np
import skimage.io
from flask import Flask, flash, request, jsonify, url_for, render_template, send_file
from werkzeug.utils import secure_filename
import time
import detector
import Compressor
from flask_cors import CORS
import json

ROOT_DIR = os.path.abspath("../")
UPLOAD_FOLDER = '/images/'

app = Flask(__name__)
CORS(app)

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
        file.save(os.path.join(ROOT_DIR + '/PROJECT_FILES/', filename))
        detector.getMask(filename, json.loads(request.form['selected']))
        results = Compressor.compressImage(filename, 'mask.png')
        response_body = jsonify(results)
        return response_body

    return 'error at file level'

@app.route('/')
def index():
    return render_template('index.html')
