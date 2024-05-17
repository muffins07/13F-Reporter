from openpyxl import Workbook, load_workbook

def init_workbook():
    wb = Workbook()
    ws = wb.active
    ws.title = 'test'
    wb.save('test.xlsx')

init_workbook()