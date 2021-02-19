# https://medium.com/aubergine-solutions/working-with-excel-sheets-in-python-using-openpyxl-4f9fd32de87f
# Working with Excel sheets in Python using openpyxl

# Appeding Group of Values at the botton of the current Sheet

from openpyxl import Workbook

wb = Workbook()
filepath = "C:/Users/Klau/Documents/Python/XLS"
file1 = "demo3.xlsx"

sheet = wb.active

data = [('Id','Name', 'Seguro'),
        (5001,'Claudia','OSDE'),
        (5002,'Juan','SETIA'),
        (1002,'Clarita','AOT')]

for row in data:
    sheet.append(row)

wb.save(filepath+'/'+file1)
