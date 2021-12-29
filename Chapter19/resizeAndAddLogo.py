import os
from PIL import Image

SQUARE_FIT_SIZE = 300
Import_filename = input("Enter File Name along with Extension : ")
Export_filename = input("Enter Export Name (without Extension) : ")
logoIm = Image.open(Import_filename)
logoWidth, logoHeight = logoIm.size

for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \
       or filename == Import_filename:
        continue

    im = Image.open(filename)
    width, height = im.size

    print('Adding logo : ' +str(filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
    im.save(Export_filename+'.png')
