from bs4 import BeautifulSoup
import requests
import pandas as pd
from collections import defaultdict
import xlsxwriter
from xlsxwriter.workbook import Workbook

# TITUS יחסית בסדר
# VESPASIAN בסדר
# domition בסדר
# NERVA יחסית בסדר
# Trajan בסדר
# Hadrian בסדר
# Antoninus pius אין מספיק
# Marcus Aurelius בסדר
# Lucius Verus אין מספיק

url_start = 'http://numismatics.org/ocre/results?q=objectType_facet%3A%22Coin%22+AND+fulltext%3A'
url_end = '&start={}'
index = 0
emp_pages_num = {'VESPASIAN': 1740, 'Titus': 1020, 'Domitian': 260, 'Nerva': 400, 'Trajan': 1200, 'Hadrian': 1400, 'Antoninus Pius': 2460,
                 'Marcus Aurelius': 3320, 'Lucius Verus': 460}
# emp_pages_num = {'VESPASIAN': 20, 'Titus': 20, 'Domitian': 20, 'Nerva': 20, 'Trajan': 20, 'Hadrian': 20, 'Antoninus Pius': 20,
#                  'Marcus Aurelius': 20, 'Lucius Verus': 20}
# http://numismatics.org/ocre/results?q=objectType_facet%3A%22Coin%22%20AND%20fulltext%3AVESPASIAN&start=20
total_pics = {}
emp_url_pics = defaultdict(list)
for key, val in emp_pages_num.items():
    print(key)
    index = 0
    pics_num = 0
    while index <= val:
        label = key
        # print(index)
        url = str(url_start + key.replace(' ', '+') + url_end.format(index))  # get url as text
        # print(url)
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'lxml')
        coins = soup.find_all('div', class_='row result-doc')  # all coins cells in the page

        for coin in coins:  # for each coin cell in the page
            # print(coin)
            pics = coin.find_all('a', class_='thumbImage', limit=1)  # finds the pictures
            if len(pics) == 1:
                # print(pics[0]['href'])
                emp_url_pics[key].append(pics[0]['href'])  # saves url pic
                pics_num += 1  # so latter we can roughly know the num,ber of pics for each emp

        index += 20
    total_pics[key] = pics_num

# saves urls
workbook = Workbook('emp url ds numismatics.xlsx')
# print(emp_url_pics.keys())
for key in emp_url_pics.keys():
    worksheet = workbook.add_worksheet(key)
    col = 0
    row = 0
    # print(key)
    for val in emp_url_pics[key]:
        # print(str(val))
        worksheet.write(row, col, str(val))
        row += 1
workbook.close()

# saves pics num
workbook_n = Workbook('emp num ds numismatics.xlsx')
worksheet_n = workbook_n.add_worksheet()
worksheet_n.write(0, 0, 'emp')
worksheet_n.write(0, 1, 'num')
col = 0
row = 1
for key, val in total_pics.items():
    worksheet_n.write(row, col, str(key))
    worksheet_n.write(row, col+1, str(val))
    row += 1
workbook_n.close()
