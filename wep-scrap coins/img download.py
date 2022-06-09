import pandas as pd
import requests
import urllib.request

df = pd.read_excel('Coins_Label.xlsx')
r = 0
la = 0
for index, row in df.iterrows():
    img_url = row['Image']
    label = row['Label']
    # if label == 'radiate':
    #     try:
    #         urllib.request.urlretrieve(img_url, 'G:/web_scraping/images/radiate/radiate_' + str(r) + '.jpg')
    #         r += 1
    #     except:
    #         print('Error')
    #         pass
    if label == 'laureate':
        try:
            urllib.request.urlretrieve(img_url, 'G:/web_scraping/images/laureate/laureate_' + str(la) + '.jpg')
            la += 1
        except:
            print('Error')
            pass