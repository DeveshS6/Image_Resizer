import os
from flask import Flask, render_template, redirect, flash, request, send_from_directory
from werkzeug.utils import secure_filename
from utils import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ImageResize'

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('Image_Resizer.html')

    if not 'file' in request.files:
        flash('No file part in request')
        return redirect(request.url)

    file = request.files.get('name')

    if file.filename == '':
        flash('No file uploaded')
        return redirect(request.url)

    file_size(file.filepath)

    if file_valid(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOADS_FOLDER'], filename))
    else:
        flash('File type not supported')
        return redirect(request.url)

    return "File uploaded successfully"

    


    