from openpyxl import Workbook, load_workbook

def main():
    wb = Workbook()
    ws = wb.active
    ws.title = 'test'

    wb.save('test.xlsx')

main()