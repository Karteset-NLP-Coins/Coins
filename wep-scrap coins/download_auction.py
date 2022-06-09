import pandas as pd
import urllib.request
import os
from xlsxwriter.workbook import Workbook

path_start = 'G:\\web_scraping\\auction DS after removing commons\\'
emperors_list = ['vespasian', 'titus', 'domitian', 'nerva', 'trajan', 'hadrian', 'antoninus pius', 'marcus aurelius', 'lucius verus']
url_start = 'https://www.acsearch.info/'

antoninus_df = pd.read_excel(path_start + 'emp_url_antoninus_after_removing_common_urls_with_other_emp.xlsx', header=None)
# print(antoninus_df)
domitian_df = pd.read_excel(path_start + 'emp_url_domitian_after_removing_common_urls_with_other_emp.xlsx', header=None)

hadrian_df = pd.read_excel(path_start + 'emp_url_hadrian_after_removing_common_urls_with_other_emp.xlsx', header=None)

lucius_df = pd.read_excel(path_start + 'emp_url_lucius_after_removing_common_urls_with_other_emp.xlsx', header=None)

marcus_df = pd.read_excel(path_start + 'emp_url_marcus_after_removing_common_urls_with_other_emp.xlsx', header=None)

nerva_df = pd.read_excel(path_start + 'emp_url_nerva_after_removing_common_urls_with_other_emp.xlsx', header=None)

titus_df = pd.read_excel(path_start + 'emp_url_titus_after_removing_common_urls_with_other_emp.xlsx', header=None)

trajan_df = pd.read_excel(path_start + 'emp_url_trajan_after_removing_common_urls_with_other_emp.xlsx', header=None)

vespasian_df = pd.read_excel(path_start + 'emp_url_vespasian_after_removing_common_urls_with_other_emp.xlsx', header=None)

emp_dict = {'antoninus': antoninus_df, 'domitian': domitian_df, 'hadrian': hadrian_df, 'lucius': lucius_df, 'marcus': marcus_df,
            'nerva': nerva_df, 'titus': titus_df, 'trajan': trajan_df, 'vespasian': vespasian_df}



cwd = os.getcwd()

directory = "auction ds"

path = os.path.join(cwd, directory)

os.mkdir(path)
new_path = cwd + '\\' + directory + '\\'

for key, val in emp_dict.items():
    emperor = key
    # print(emperor)
    not_working_urls = []
    emperor_path = new_path + '\\' + emperor + '\\'
    # print(emperor_path)
    path = os.path.join(new_path, emperor)
    os.mkdir(path)
    image_num = 0
    for i, row in val.iterrows():
        img_url = url_start + str(val[0][i])
        try:
            urllib.request.urlretrieve(img_url, emperor_path + str(image_num) + '.jpg')
            image_num += 1
        except:
            not_working_urls.append(img_url)
            pass
    # try:
    #     workbook = Workbook('not_working_urls_' + key + '.xlsx')
    #     worksheet = workbook.add_worksheet()
    #     # print(emp_url_pics.keys())
    #     row = 0
    #     for link in not_working_urls:
    #         worksheet.write(row, 0, str(link))
    #         row += 1
    #     workbook.close()
    # except:
    #     print('e squared')
