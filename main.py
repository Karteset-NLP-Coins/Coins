from bs4 import BeautifulSoup
import requests
import pandas as pd

right_url_start = 'http://numismatics.org/'
all_data = []
radiate_laureate_classifier = []

index = 0
while index <= 2060:
    label = 'radiate'
    print(index)
    radiate_url = 'http://numismatics.org/ocre/results?q=objectType_facet%3A%22Coin%22+AND+fulltext%3ARadiate+AND+fulltext%3Ahead&start={}'.format(index)
    radiate_html_text = requests.get(radiate_url).text
    radiate_soup = BeautifulSoup(radiate_html_text, 'lxml')
    coins = radiate_soup.find_all('div', class_='row result-doc')

    for coin in coins:
        pics = coin.find_all('a', class_='thumbImage', limit=2)
        if len(pics) == 2:# and right_url_start in (pics[0]['href'] and pics[1]['href']):
            Single_coin_data = {}
            Classifier_data = {}
            head_line = coin.find('a', href=True).text
            info = coin.find('dl', 'dl-horizontal')
            Single_coin_data['Header'] = head_line
            Single_coin_data['Pic_Obverse'] = pics[0]['href']
            Single_coin_data['Pic_Reverse'] = pics[1]['href']
            for dt, dd in zip(info.select('dt'), info.select('dd')):
                Single_coin_data[dt.text.strip()] = dd.text.strip()

            if label in Single_coin_data['Obverse']:
                Classifier_data['Image'] = pics[0]['href']
            # else:
            #     Classifier_data['Image'] = pics[1]['href']
                Classifier_data['Label'] = label

                radiate_laureate_classifier.append(Classifier_data)
                all_data.append(Single_coin_data)

    index += 20

index = 0
while index <= 12060:
    label = 'laureate'
    print(index)
    radiate_url = 'http://numismatics.org/ocre/results?q=fulltext%3Alaureate%20AND%20fulltext%3Ahead%20AND%20objectType_facet%3A%22Coin%22&start={}'.format(index)
    radiate_html_text = requests.get(radiate_url).text
    radiate_soup = BeautifulSoup(radiate_html_text, 'lxml')
    coins = radiate_soup.find_all('div', class_='row result-doc')

    for coin in coins:
        pics = coin.find_all('a', class_='thumbImage', limit=2)
        if len(pics) == 2:# and right_url_start in (pics[0]['href'] and pics[1]['href']):
            Single_coin_data = {}
            Classifier_data = {}
            head_line = coin.find('a', href=True).text
            info = coin.find('dl', 'dl-horizontal')
            Single_coin_data['Header'] = head_line
            Single_coin_data['Pic_Obverse'] = pics[0]['href']
            Single_coin_data['Pic_Reverse'] = pics[1]['href']
            for dt, dd in zip(info.select('dt'), info.select('dd')):
                Single_coin_data[dt.text.strip()] = dd.text.strip()

            if label in Single_coin_data['Obverse']:
                Classifier_data['Image'] = pics[0]['href']
            # else:
            #     Classifier_data['Image'] = pics[1]['href']
                Classifier_data['Label'] = label

                radiate_laureate_classifier.append(Classifier_data)
            all_data.append(Single_coin_data)

    index += 20

df = pd.DataFrame(radiate_laureate_classifier)
df.to_excel('Coins_Label.xlsx', sheet_name='sheet1', index=False)

df = pd.DataFrame(all_data)
df.to_excel('Coins_Full_Data.xlsx', sheet_name='sheet1', index=False)

# coin = soup.find('div', class_='row result-doc')
# head_line = coin.find('a', href=True).text
# info = coin.find('dl', 'dl-horizontal')
# pics = coin.find_all('a', class_='thumbImage', limit=2)
# print("emp " + head_line)
# print(info.getText())
# d = {}
# for dt, dd in zip(soup.select('dt'), soup.select('dd')):
#     d[dt.text.strip()] = dd.text.strip().splitlines()
# print(d)
# print(pics)
#
# for pic in pics:
#     print(pic['href'])
# print(pics[0]['href'])
# print(pics[1]['href'])
# print('')
