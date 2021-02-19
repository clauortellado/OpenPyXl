# Copy data from one sheet to another sheet

from openpyxl import load_workbook

filepath="C:/Users/Klau/Documents/Python/XLS/"
file1 = "demo4.xlsx"
file2 = "demo5.xlsx"
wb = load_workbook(filepath+file1)

# get sheet
source = wb.get_sheet_by_name("Sheet")

# copy sheet
target = wb.copy_worksheet(source)

# save
wb.save(filepath+file2)
