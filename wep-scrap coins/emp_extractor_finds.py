import openpyxl
from bs4 import BeautifulSoup
import requests
import pandas as pd
from collections import defaultdict
import xlsxwriter
from xlsxwriter.workbook import Workbook

# TITUS ~ 3000
# VESPASIAN ~ 600
# domition ~ 1900
# NERVA ~ 850
# Trajan ~ 3600
# Hadrian ~ 3900
# Antoninus pius ~ 3900
# Marcus Aurelius ~ 3100
# Lucius Verus ~ 300

pic_url = 'https://finds.org.uk'
url_start = 'https://finds.org.uk/database/search/results/q/'
url_end = '/objectType/COIN/show/100/page/{}'

# emp : number of pages
emp_pages_num = {'VESPASIAN': 32, 'Titus': 6, 'Domitian': 20, 'Nerva': 9, 'Trajan': 40, 'Hadrian': 43, 'Antoninus Pius': 43,
                 'Marcus Aurelius': 32, 'Lucius Verus': 4}
# emp_pages_num = {'VESPASIAN': 1, 'Titus': 1}
total_pics = {}
emp_url_pics = defaultdict(list)
for key, val in emp_pages_num.items():
    print(key)
    page = 1
    pics_num = 0
    while page <= val + 1:
        url = str(url_start + key.replace(' ', '+') + url_end.format(page))
        # print(url)
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'lxml')
        coins = soup.find_all('div', typeof='crm:E22_Man-Made_Object')  # all coins cells in the page
        # print(coins)
        for coin in coins:
            # print(coin)
            pics = coin.find_all('a', limit=1)  # finds the pictures
            if len(pics) == 1:
                pic = pics[0]['href']
                pic = pic_url + pic
                emp_url_pics[key].append(pic)
                pics_num += 1
        page += 1
    total_pics[key] = pics_num

# saves urls
workbook = Workbook('emp url ds finds.xlsx')
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
workbook_n = Workbook('emp num ds finds.xlsx')
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