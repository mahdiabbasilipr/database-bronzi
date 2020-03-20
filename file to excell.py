import databasev3
from openpyxl import Workbook

list_data = databasev3.get_list_data('/home/mahdi/Documents/python project/project bronzi/V1/data.txt')
wb = Workbook()
# wb.active()

ws1 = wb.create_sheet('sheet')

ws1['A1'] = 'نام محصول'
ws1['B1'] = 'کد محصول'
ws1['C1'] = 'وزن'
ws1['D1'] = 'قد'
ws1['E1'] = 'عرض'
ws1['F1'] = 'قیمت برای ما علیرضا'
ws1['G1'] = 'قیمت برای ما وزن'
ws1['H1'] = 'قیمت برای مشتری'

price_of_bronze = 0
temp = 1
for item in list_data:
    temp += 1
    temp = str(temp)

    ws1['A' + temp] = item['name']
    ws1['B' + temp] = item['code']
    ws1['C' + temp] = item['weight']
    ws1['D' + temp] = item['hight']
    ws1['E' + temp] = item['width']
    ws1['F' + temp] = item['price']
    ws1['G' + temp] = item['weight'] * price_of_bronze
    ws1['H' + temp] = item['price']+(item['price'] * 30) / 100

    temp = int(temp)

wb.save(filename='e1.xlsx')
