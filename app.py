import PIL
import glob
from PIL import Image

import os
from flask import Flask, render_template, redirect, flash, request, send_from_directory
from werkzeug.utils import secure_filename
from utils import *

app = Flask(__name__)
app.config['UPLOADS_FOLDER'] = UPLOADS_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.config['SECRET_KEY'] = 'ImageResize'

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('Image_Resizer.html')

    if not 'file' in request.files:
        flash('No file part in request')
        return redirect(request.url)

    file = request.form['snap']
    
    print(file) 
    if file.filename == '':
        flash('No file uploaded')
        return redirect(request.url)

    if file_valid(file.filename):

        # base_width = 360
        # image = Image.open(file.filename)
        # print(image)
        # width_percent = (base_width / float(image.size[0]))
        # hsize = int((float(image.size[1]) * float(width_percent)))
        # image = image.resize((base_width, hsize), PIL.Image.ANTIALIAS)
        # image.save('resized_compressed_image.jpg')

        
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOADS_FOLDER'], filename))
        flash('Image uploaded successfully')
    else:
        flash('File type not supported')
        return redirect(request.url)

    return render_template('Image_Resizer.html')

    


    