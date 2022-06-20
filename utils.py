import os
from flask import flash, redirect, request

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg',]
UPLOADS_FOLDER = 'uploads/images/'
ALLOWED_SIZE = 2097152

def file_valid(file):
  return '.' in file and \
    file.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS 

def file_size(path):
    if os.path.getsize(path) > ALLOWED_SIZE:
        flash('File size too large, upload smaller image')
        return redirect(request.url)
    return 
        

