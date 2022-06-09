import pandas as pd
from xlsxwriter.workbook import Workbook

antoninus_df = pd.read_excel('emp_url_antoninus_with_filtering.xlsx', header=None)  # can also index sheet by name or fetch all sheets
antoninus_list = antoninus_df[0].tolist()

domitian_df = pd.read_excel('emp_url_domitian_with_filtering.xlsx', header=None)  # can also index sheet by name or fetch all sheets
domitian_list = domitian_df[0].tolist()

hadrian_df = pd.read_excel('emp_url_hadrian_with_filtering.xlsx', header=None)  # can also index sheet by name or fetch all sheets
hadrian_list = hadrian_df[0].tolist()

lucius_df = pd.read_excel('emp_url_lucius_with_filtering.xlsx', header=None)  # can also index sheet by name or fetch all sheets
lucius_list = lucius_df[0].tolist()

marcus_df = pd.read_excel('emp_url_marcus_with_filtering.xlsx', header=None)  # can also index sheet by name or fetch all sheets
marcus_list = marcus_df[0].tolist()

nerva_df = pd.read_excel('emp_url_nerva_with_filtering.xlsx', header=None)  # can also index sheet by name or fetch all sheets
nerva_list = nerva_df[0].tolist()

titus_df = pd.read_excel('emp_url_titus_with_filtering.xlsx', header=None)  # can also index sheet by name or fetch all sheets
titus_list = titus_df[0].tolist()

trajan_df = pd.read_excel('emp_url_trajan_with_filtering.xlsx', header=None)  # can also index sheet by name or fetch all sheets
trajan_list = trajan_df[0].tolist()

vespasian_df = pd.read_excel('emp_url_vespasian_with_filtering.xlsx', header=None)  # can also index sheet by name or fetch all sheets
vespasian_list = vespasian_df[0].tolist()

emp_lists = [antoninus_list, domitian_list, hadrian_list, lucius_list, marcus_list, nerva_list, titus_list, trajan_list, vespasian_list]
emp_names = ['antoninus', 'domitian', 'hadrian', 'lucius', 'marcus', 'nerva', 'titus', 'trajan', 'vespasian']
# emp_dict_list = {'antoninus': antoninus_list, 'domitian': domitian_list, 'hadrian': hadrian_list, 'lucius': lucius_list, 'marcus': marcus_list,
#                  'nerva': nerva_list, 'titus': titus_list, 'trajan': trajan_list, 'vespasian': vespasian_list}

common_element_list = []
for i in range(len(emp_lists)):
    for j in range(i + 1, len(emp_lists)):
        common_element_list.extend(list(set(emp_lists[i]).intersection(emp_lists[j])))

for emp_list, emp_name in zip(emp_lists, emp_names):
    print(f'working on {emp_name}')
    emp = [x for x in emp_list if x not in common_element_list]
    try:
        workbook = Workbook('emp_url_' + emp_name + '_after_removing_common_urls_with_other_emp.xlsx')
        worksheet = workbook.add_worksheet(emp_name)
        # print(emp_url_pics.keys())
        row = 0
        for link in emp:
            worksheet.write(row, 0, str(link))
            row += 1
        workbook.close()
    except:
        print('e squared')

print(f'working on common urls')
try:
    workbook = Workbook('common_urls.xlsx')
    worksheet = workbook.add_worksheet()
    # print(emp_url_pics.keys())
    row = 0
    for link in common_element_list:
        worksheet.write(row, 0, str(link))
        row += 1
    workbook.close()
except:
    print('e squared')