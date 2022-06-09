import pandas as pd
import urllib.request
import os
from xlsxwriter.workbook import Workbook

path_start = 'G:\\web_scraping\\coin xlsx up to 6.6.22\\emp coin xlsx finds and numismatics\\'
emperors_list = ['vespasian', 'titus', 'domitian', 'nerva', 'trajan', 'hadrian', 'antoninus pius', 'marcus aurelius', 'lucius verus']

# removing dups
antoninus_df = pd.read_excel(path_start + 'emp url ds finds.xlsx', header=None, sheet_name='Antoninus Pius')
antoninus_list = list(dict.fromkeys(antoninus_df[0].tolist()))

domitian_df = pd.read_excel(path_start + 'emp url ds finds.xlsx', header=None, sheet_name='Domitian')
domitian_list = list(dict.fromkeys(domitian_df[0].tolist()))

hadrian_df = pd.read_excel(path_start + 'emp url ds finds.xlsx', header=None, sheet_name='Hadrian')
hadrian_list = list(dict.fromkeys(hadrian_df[0].tolist()))

lucius_df = pd.read_excel(path_start + 'emp url ds finds.xlsx', header=None, sheet_name='Lucius Verus')
lucius_list = list(dict.fromkeys(lucius_df[0].tolist()))

marcus_df = pd.read_excel(path_start + 'emp url ds finds.xlsx', header=None, sheet_name='Marcus Aurelius')
marcus_list = list(dict.fromkeys(marcus_df[0].tolist()))

nerva_df = pd.read_excel(path_start + 'emp url ds finds.xlsx', header=None, sheet_name='Nerva')
nerva_list = list(dict.fromkeys(nerva_df[0].tolist()))

titus_df = pd.read_excel(path_start + 'emp url ds finds.xlsx', header=None, sheet_name='Titus')
titus_list = list(dict.fromkeys(titus_df[0].tolist()))

trajan_df = pd.read_excel(path_start + 'emp url ds finds.xlsx', header=None, sheet_name='Trajan')
trajan_list = list(dict.fromkeys(trajan_df[0].tolist()))

vespasian_df = pd.read_excel(path_start + 'emp url ds finds.xlsx', header=None, sheet_name='VESPASIAN')
vespasian_list = list(dict.fromkeys(vespasian_df[0].tolist()))

emp_lists = [antoninus_list, domitian_list, hadrian_list, lucius_list, marcus_list, nerva_list, titus_list, trajan_list, vespasian_list]
emp_names = ['antoninus', 'domitian', 'hadrian', 'lucius', 'marcus', 'nerva', 'titus', 'trajan', 'vespasian']

# removing common urls
common_element_list = []
for i in range(len(emp_lists)):
    for j in range(i + 1, len(emp_lists)):
        common_element_list.extend(list(set(emp_lists[i]).intersection(emp_lists[j])))
# print(len(common_element_list))
emp_dict = {}
for emp_list, emp_name in zip(emp_lists, emp_names):
    # print(f'working on {emp_name}')
    new_emp_list = [x for x in emp_list if x not in common_element_list]
    emp_dict[emp_name] = pd.DataFrame(new_emp_list)

# emp_dict = {'antoninus': antoninus_df, 'domitian': domitian_df, 'hadrian': hadrian_df, 'lucius': lucius_df, 'marcus': marcus_df,
#             'nerva': nerva_df, 'titus': titus_df, 'trajan': trajan_df, 'vespasian': vespasian_df}

cwd = os.getcwd()

directory = "finds ds"

path = os.path.join(cwd, directory)

os.mkdir(path)
new_path = cwd + '\\' + directory + '\\'

for key, val in emp_dict.items():
    emperor = key
    print(emperor)
    not_working_urls = []
    emperor_path = new_path + '\\' + emperor + '\\'
    # print(emperor_path)
    path = os.path.join(new_path, emperor)
    os.mkdir(path)
    image_num = 0
    for i, row in val.iterrows():
        img_url = str(val[0][i])
        if img_url.endswith(('.png', 'PNG', 'JPG', 'jpg')):
            try:
                urllib.request.urlretrieve(img_url, emperor_path + str(image_num) + '.jpg')
                image_num += 1
            except:
                not_working_urls.append(img_url)
                pass
