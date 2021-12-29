import os
from PIL import Image

for foldername, subfolders, filenames in os.walk('D:\Important Files'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        if not filename.endswith(('.png','.jpg')):
            numNonPhotoFiles += 1
            continue

        img = None
        try :
            img = Image.open(foldername + '/' + filename)
        except:
            continue

        width, heigth = img.size
        if width > 500 and heigth > 500:
            numPhotoFiles += 1
        else:
            numNonPhotoFiles += 1

    if numPhotoFiles > (numPhotoFiles + numNonPhotoFiles) / 2:
        print(foldername)
