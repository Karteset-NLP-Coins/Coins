import openpyxl
from bs4 import BeautifulSoup
import requests
import pandas as pd
from collections import defaultdict
import xlsxwriter
from xlsxwriter.workbook import Workbook
from selenium import webdriver
import time

# TITUS ~ 3000
# VESPASIAN ~ 600
# domition ~ 1900
# NERVA ~ 850
# Trajan ~ 3600
# Hadrian ~ 3900
# Antoninus pius ~ 3900
# Marcus Aurelius ~ 3100
# Lucius Verus ~ 300


# https://www.acsearch.info/home.html

# titus urls
# url1 = 'https://www.acsearch.info/search.html?term=Titus&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=0'
# url2 = 'https://www.acsearch.info/search.html?term=Titus&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=1'
# url3 = 'https://www.acsearch.info/search.html?term=Titus&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=2'
# url4 = 'https://www.acsearch.info/search.html?term=Titus&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=3'
# url5 = 'https://www.acsearch.info/search.html?term=Titus&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=4'

# vespasian
# url1 = 'https://www.acsearch.info/search.html?term=Vespasian&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=0'
# url2 = 'https://www.acsearch.info/search.html?term=Vespasian&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=1'
# url3 = 'https://www.acsearch.info/search.html?term=Vespasian&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=2'
# url4 = 'https://www.acsearch.info/search.html?term=Vespasian&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=3'
# url5 = 'https://www.acsearch.info/search.html?term=Vespasian&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=4'

# # Domitian
# url1 = 'https://www.acsearch.info/search.html?term=Domitian&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=0'
# url2 = 'https://www.acsearch.info/search.html?term=Domitian&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=1'
# url3 = 'https://www.acsearch.info/search.html?term=Domitian&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=2'
# url4 = 'https://www.acsearch.info/search.html?term=Domitian&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=3'
# url5 = 'https://www.acsearch.info/search.html?term=Domitian&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=4'

# Antoninus pius
# url1 = 'https://www.acsearch.info/search.html?term=Antoninus+pius&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=0'
# url2 = 'https://www.acsearch.info/search.html?term=Antoninus+pius&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=1'
# url3 = 'https://www.acsearch.info/search.html?term=Antoninus+pius&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=2'
# url4 = 'https://www.acsearch.info/search.html?term=Antoninus+pius&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=3'
# url5 = 'https://www.acsearch.info/search.html?term=Antoninus+pius&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=4'

# # Nerva
# url1 = 'https://www.acsearch.info/search.html?term=Nerva&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=0'
# url2 = 'https://www.acsearch.info/search.html?term=Nerva&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=1'
# url3 = 'https://www.acsearch.info/search.html?term=Nerva&category=1-2&lot=&thesaurus=1&images=1&en1&currency=usd&order=2'
# url4 = 'https://www.acsearch.info/search.html?term=Nerva&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=3'
# url5 = 'https://www.acsearch.info/search.html?term=Nerva&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=4'

# Trajan
# url1 = 'https://www.acsearch.info/search.html?term=Trajan&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=0'
# url2 = 'https://www.acsearch.info/search.html?term=Trajan&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=1'
# url3 = 'https://www.acsearch.info/search.html?term=Trajan&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=2'
# url4 = 'https://www.acsearch.info/search.html?term=Trajan&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=3'
# url5 = 'https://www.acsearch.info/search.html?term=Trajan&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=4'

# Hadrian
# url1 = 'https://www.acsearch.info/search.html?term=Hadrian&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=0'
# url2 = 'https://www.acsearch.info/search.html?term=Hadrian&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=1'
# url3 = 'https://www.acsearch.info/search.html?term=Hadrian&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=2'
# url4 = 'https://www.acsearch.info/search.html?term=Hadrian&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=3'
# url5 = 'https://www.acsearch.info/search.html?term=Hadrian&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=4'

# Marcus Aurelius
# url1 = 'https://www.acsearch.info/search.html?term=Marcus+Aurelius&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=0'
# url2 = 'https://www.acsearch.info/search.html?term=Marcus+Aurelius&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=1'
# url3 = 'https://www.acsearch.info/search.html?term=Marcus+Aurelius&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=2'
# url4 = 'https://www.acsearch.info/search.html?term=Marcus+Aurelius&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=3'
# url5 = 'https://www.acsearch.info/search.html?term=Marcus+Aurelius&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=4'

# # Lucius Verus
url1 = 'https://www.acsearch.info/search.html?term=Lucius+Verus&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=0'
url2 = 'https://www.acsearch.info/search.html?term=Lucius+Verus&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=1'
url3 = 'https://www.acsearch.info/search.html?term=Lucius+Verus&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=2'
url4 = 'https://www.acsearch.info/search.html?term=Lucius+Verus&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=3'
url5 = 'https://www.acsearch.info/search.html?term=Lucius+Verus&category=1-2&lot=&thesaurus=1&images=1&en=1&currency=usd&order=4'

curr_emp = 'lucius'
# all_emp_list = ['vespasian', 'titus', 'domitian', 'nerva', 'trajan', 'hadrian', 'antoninus pius', 'marcus aurelius', 'lucius verus']
urls = [url1, url2, url3, url4, url5]
time_sleep = 20
emp_url_pics = []
coins_num = 0
for url in urls:
    print(f'order {url[-1]}')
    coins_num = 0
    # Web scrapper for infinite scrolling page
    driver = webdriver.Chrome(executable_path=r"G:\chromedriver_win32\chromedriver.exe")
    driver.get(url)
    time.sleep(time_sleep)  # Allow 2 seconds for the web page to open
    # scroll_pause_time = 1  # You can set your own pause time. My laptop is a bit slow so I use 1 sec
    screen_height = driver.execute_script("return window.screen.height;")  # get the screen height of the web
    # i = 1
    #
    # while True:
    #     # scroll one screen height each time
    #     driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    #     i += 1
    #     time.sleep(scroll_pause_time)
    #     # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    #     scroll_height = driver.execute_script("return document.body.scrollHeight;")
    #     # Break the loop when the height we need to scroll to is larger than the total scroll height
    #     if (screen_height) * i > scroll_height:
    #         break

    ##### Extract Reddit URLs #####

    soup = BeautifulSoup(driver.page_source, "html.parser")
    Coins = soup.find_all('div', class_='auction-lot')
    # print(Coins)
    for Coin in Coins:
        coins_num += 1
        # print(Coin)
        pic = Coin.find_all('img', limit=1)
        text = Coin.find_all('div', class_='lot-desc')[0].span.text.lower().split()[:10]
        # print(text)
        if curr_emp in text:
            pic_url = pic[0]['src']
            # print(pic_url)
            emp_url_pics.append(pic_url)
    print(coins_num)

emp_url_pics = list(dict.fromkeys(emp_url_pics))  # remove dups
print(f'total pics in this site for {curr_emp} {len(emp_url_pics)}')
try:
    workbook = Workbook('emp_url_' + curr_emp + '_with_filtering.xlsx')
    worksheet = workbook.add_worksheet(curr_emp)
    # print(emp_url_pics.keys())
    row = 0
    for link in emp_url_pics:
        worksheet.write(row, 0, str(link))
        row += 1
    workbook.close()
except:
    print('e squared')
