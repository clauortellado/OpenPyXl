# https://medium.com/aubergine-solutions/working-with-excel-sheets-in-python-using-openpyxl-4f9fd32de87f
# Working with Excel sheets in Python using openpyxl

# Create an Excel Sheet__________________
from openpyxl import Workbook

wb = Workbook()

filepath = "C:/Users/Klau/Documents/Python/XLS"

wb.save (filepath+"/demo1.xlsx")
