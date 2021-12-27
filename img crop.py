from PIL import Image
import os

directoryr = 'G:/web_scraping/images/radiate'
directoryl = 'G:/web_scraping/images/laureate'

for filename in os.listdir(directoryl):
    if filename.endswith(".jpg"):
        im = Image.open(directoryl + '/' + filename)
        width, height = im.size
        if width == 1300:
            im = im.crop((0, 0, width / 2, height))
            im.save(filename)
