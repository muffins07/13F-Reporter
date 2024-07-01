import pandas as pd
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from pdf_parser import df
from pos_parser import fcm_pos_df, get_positions

def filter_char(df, col_name, proc):
    '''
    Removes character from CUSIPs in 
            13F or FCM positions dataframes
    Inputs: 13F or FCM positions dataframe (df), 
            CUSIP column (col_name), 
            procedure (proc)
    Output: 13F or FCM positions dataframe with a 
            CUSIP column lacking whitespace or
            an apostrophe
    '''
    filter_chars = [' ', '\'', ',']
    if proc == 0:
        df[col_name] = df[col_name].str.replace(filter_chars[0], '')
    elif proc == 1:
        df[col_name] = df[col_name].str.replace(filter_chars[1], '')
    elif proc == 2:
        df[col_name] = df[col_name].str.replace(filter_chars[2], '')
    return df

def format_df(df, proc):
    '''
    Formats 13F or FCM positions dataframes using a given procedure
    Inputs: dataframe (df), procedure (proc)
    Output: Cusip column with no whitespace/apostrophe
    '''
    df = filter_char(df, 'Cusip', proc)
    return df

def format_with_commas(value):
    return '{:,}'.format(value)

def fit_cols_to_text(df):
    excel_writer = pd.ExcelWriter('C:\\Users\\intern1\\Desktop\\13F_Reporter\\Information Table.xlsx', engine='openpyxl')
    df.to_excel(excel_writer, index=False, sheet_name='InformationTable')
    workbook = excel_writer.book
    worksheet = workbook['InformationTable']

    for col_cells in worksheet.columns:
        max_length = 0
        col = col_cells[0].column_letter
        for cell in col_cells:
            try: # Avoids error on empty cells
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = (max_length + 2) * 1.2
        worksheet.column_dimensions[col].width = adjusted_width
    
    excel_writer.close() # safer than save()?
    return df

def format_merged_df(info_table):
    # Build report
    desired_cols = {
        0:'NAME OF ISSUER', 
        1:'TITLE OF CLASS', 
        2:['CUSIP', 'FIGI'],
        3:'VALUE (to the nearest $)',
        4:['SHARES OR PRN AMOUNT', 'SH/PRN', 'PUT/CALL'],
        5:'INVESTMENT DISCRETION', 
        6:'OTHER MANAGER', 
        7:'VOTING AUTHORITY', # not currently in-use
        8:['SOLE', 'SHARED', 'NONE']
    } # Based on ToppanMerril's 13F info table worksheet at: https://www.toppanmerrill.com/sec-edgar-resources/form-13f/
    
    # Rename columns from 13F & FCM dataframes
    if 'Description' in info_table.columns:
        info_table = info_table.rename(columns={'Description': desired_cols[0]})
    if 'Issue' in info_table.columns:
        info_table = info_table.rename(columns={'Issue': desired_cols[1]})
    if 'Cusip' in info_table.columns:
        info_table = info_table.rename(columns={'Cusip': desired_cols[2][0]})
    if 'CurrVal' in info_table.columns:
        info_table = info_table.rename(columns={'CurrVal': desired_cols[3]})
    if 'Quantity' in info_table.columns:
        info_table = info_table.rename(columns={'Quantity': desired_cols[4][0]})
    
    # Inserts necessary columns
    info_table.insert(loc=3, column=desired_cols[2][1], value='') # why does this work when I don't assign it to info_table var
    info_table.insert(loc=6, column=desired_cols[4][1], value='SH')
    info_table.insert(loc=7, column=desired_cols[4][2], value='')
    info_table.insert(loc=8, column=desired_cols[5],    value='SOLE')
    info_table.insert(loc=9, column=desired_cols[6],    value='')
    info_table.insert(loc=10,column=desired_cols[8][0], value='') # value should be quantities again
    info_table[desired_cols[8][0]] = info_table[desired_cols[4][0]]
    
    info_table.insert(loc=11,column=desired_cols[8][1], value='')
    info_table.insert(loc=12,column=desired_cols[8][2], value='')
    
    # Format report
    info_table = info_table.sort_values(by=desired_cols[0]) # Sort alphabetically
    if desired_cols[3] in info_table.columns:
        info_table[desired_cols[3]] = info_table[desired_cols[3]].astype(int)
        info_table[desired_cols[3]] = info_table[desired_cols[3]].apply(format_with_commas)
    if desired_cols[4][0] in info_table.columns:
        info_table[desired_cols[4][0]] = info_table[desired_cols[4][0]].astype(int)
        info_table[desired_cols[4][0]] = info_table[desired_cols[4][0]].apply(format_with_commas)
    if desired_cols[8][0] in info_table.columns:
        info_table[desired_cols[8][0]] = info_table[desired_cols[8][0]].astype(int)
        info_table[desired_cols[8][0]] = info_table[desired_cols[8][0]].apply(format_with_commas)
    # if desired_cols[3] in info_table.columns:
    #     info_table = filter_char(info_table, )
    #     info_table[desired_cols[3]] = info_table[desired_cols[3]].astype(int)


    # info_table.to_excel('C:\\Users\\intern1\\Desktop\\13F_Reporter\\Information Table.xlsx', )

    return info_table

def merge(df1, df2):
    '''
    Combines 13F & positions based on matching Cusip entries
    Inputs: 13F (df1) & FCM positions (df2) dataframes
    Output: intersection of 13F & FCM positions dataframes
    '''
    merged_df = pd.merge(df1, df2, how='inner', on='Cusip')
    result_df = merged_df[['Description', 'Issue', 'Cusip', 'CurrVal', 'Quantity']]
    formatted_df = format_merged_df(result_df)
    final_df = fit_cols_to_text(formatted_df)
    return final_df

pdf_df = df # instantiates 13f df
fcm_pos_df = get_positions(fcm_pos_df) # instantiates fcm pos

format_df(pdf_df, 0) # formats 13F
format_df(fcm_pos_df, 1) # formats FCM positions

sec_report = merge(pdf_df, fcm_pos_df) # instantiates merged df

# __name__ == 'main' should be here

# Notes:
# - It seems like some text beloning to the Title of Class column is cut off
#   Instead, it's still in the Name of Issuer column
#   Or vice versa.
#   Examples: see rows for Berkshire Hathaway (missing DEL) & SPDR Dow Jones (includes UT SER 1) 