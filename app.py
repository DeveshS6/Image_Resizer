import os
from flask import Flask, render_template, redirect, flash, request, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ImageResize'

@app.route('/')
def index():
    return render_template('Image_Resizer.html')