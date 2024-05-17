from openpyxl import Workbook, load_workbook
import pandas as pd

def main():
    wb = load_workbook('test.xlsx')
    ws = wb.active

    df = pd.read_excel('test.xlsx')
    num_rows = df.shape[0]
    
    work_sheet = ws
    row_count = num_rows
    rem_white_space(work_sheet, row_count)

    wb.save('test (no whitespace).xlsx')

def rem_white_space(xl_file, row_num):
    # removes whitespace from CUSIP column
    for row in range(2, row_num+1):
        cusip = xl_file['A' + str(row)].value
        xl_file['A' + str(row)].value = cusip.replace(" ", "")

main()