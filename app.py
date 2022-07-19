from pickletools import optimize
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
        return render_template('image_resizer.html')
    return 

@app.route('/upload', methods=['GET','POST'])
def upload():
    flash("ok 0")
    file = request.files.get('file')
    
    if not 'file' in request.files:
        flash('No file part in request')
        return "NO file"
    flash("ok 1")
   
    
    print(file) 
    flash("ok 2")
    if file.filename == '':
        flash('No file uploaded')
        return "No file uploaded"

    if file_valid(file.filename):
        
        print(file.filename)
        filename = secure_filename(file.filename)
        print(filename)
        file.save(os.path.join(app.config['UPLOADS_FOLDER'], filename))
        flash('Image uploaded successfully 1')

        image_path = "uploads/images/"+filename
        print(image_path)
        

        base_width = 360
        image = Image.open(image_path)
        
        width_percent = (base_width / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(width_percent)))
        image = image.resize((base_width, hsize), PIL.Image.ANTIALIAS)
        print(image)
        new_filename_path = image_path+"_compressed.PNG"
        image.save(new_filename_path , optimize=True)

        
        # file.save(os.path.join(app.config['UPLOADS_FOLDER'], 'resized_compressed_image.jpg'))
        # flash('Image uploaded successfully 2')
    else:
        flash('File type not supported')
        return redirect(request.url)

    return render_template('image_resizer.html')

    


    