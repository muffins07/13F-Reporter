from openpyxl import Workbook, load_workbook
import pandas as pd

wb = load_workbook('test.xlsx')
ws = wb.active

df = pd.read_excel('test.xlsx')
num_rows = df.shape[0]

for row in range(2, num_rows+1):
    cusip = ws['A' + str(row)].value
    ws['A' + str(row)].value = cusip.replace(" ", "")

wb.save('test_modified.xlsx')

# software ideas
# - don't require empty .xlsx file; create programmatically
# - create app distributible .exe
# - github for project
# - tech used: pandas, openpyxl
# - libraries downloaded (not necessarily in-use): pandas, openpyxl, tika
# - 13F_PDF_Convertor.py is from: https://www.youtube.com/watch?v=4AFepZ8L7xw