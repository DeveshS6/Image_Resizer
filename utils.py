import os
from flask import flash, redirect, request

ALLOWED_EXTENSIONS = ['PNG', 'jpg', 'jpeg', 'png', 'JPG', 'JPEG']
UPLOADS_FOLDER = 'uploads/images'


def file_valid(file):
  return '.' in file and \
    file.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS 

        

