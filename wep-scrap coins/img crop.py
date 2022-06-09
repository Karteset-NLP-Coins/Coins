from PIL import Image
import os
import scipy.ndimage

directoryr = 'G:/web_scraping/images/radiate'
directoryl = 'G:/web_scraping/images/laureate'
i=0
for filename in os.listdir(directoryl):
    if filename.endswith(".jpg"):
        # i+=1
        im = Image.open(directoryl + '/' + filename)
        if not im.mode == 'RGB':
            print(filename)
            print(im.mode)

        # width, height = im.size
        # if width == 1300:
        #     im = im.crop((0, 0, width / 2, height))
        #     im.save(filename)
print(i)
# dict = ['212', '852', '853', '874']
#
# for filename in dict:
#     im = Image.open(directoryr + '/radiate_' + filename+'.jpg')
#     width, height = im.size
#     im = im.crop((0, 0, width / 2, height))
#     im.save('radiate_' + filename+'.jpg')
