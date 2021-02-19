# Remove Sheet from Existing XLSX

from openpyxl import load_workbook

filepath = "C:/Users/Klau/Documents/Python/XLS/"
file1 = "demo4.xlsx"
wb = load_workbook(filepath+file1)

wb.remove(wb.get_sheet_by_name("Sheet2"))
wb.save(filepath+file1)