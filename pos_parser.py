import pandas as pd
import pyodbc as odbc
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

server = 'NEWSERVER\PORTFOLIOCENTER'
database = 'PortfolioCenter'
username = 'PyDev'
password = 'Intern2024'

fcm_pos_df = None

def get_positions(dataframe):
    '''
    Connects to PortFolioCenter and positions table 
    Input: SQL table
    Output: dataframe of SQL table
    '''
    stored_proc = 'FCM_Sp_13Fpositions'
    conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    conn_url = URL.create('mssql+pyodbc', query={'odbc_connect': conn_str})
    engine = create_engine(conn_url, module=odbc)
    dataframe = pd.read_sql_query(f'EXEC {stored_proc}', engine)

    append_dataframe(dataframe, '13F Positions')
    return dataframe

def append_dataframe(dataframe, sheet_title):
     '''
     Appends 13F Positions table to xl workbook (what purpose does workbook have)
     Inputs: workbook dataframe, sheet name
     Output: excel workbook with some given sheet appended
     '''
     wb_path = 'C:\\Users\\intern1\\Desktop\\13F_Reporter\\fcm.xlsx'
     # bug: if user names xl file anything other than "fcm," error occurs

     with pd.ExcelWriter(wb_path, engine='openpyxl', mode='a') as writer:
         dataframe.to_excel(writer, sheet_name=sheet_title, index=False)