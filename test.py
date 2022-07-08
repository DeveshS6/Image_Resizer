import PIL
from PIL import Image
from tkinter.filedialog import *

file_path = askopenfilename()
# print(file_path)
image = PIL.Image.open(file_path)
base_width = 360

width_percent = (base_width / float(image.size[0]))
hsize = int((float(image.size[1]) * float(width_percent)))

image = image.resize((base_width, hsize), PIL.Image.ANTIALIAS)

save_path = asksaveasfilename()

image.save(save_path+"_compressed.PNG", quality = 25)