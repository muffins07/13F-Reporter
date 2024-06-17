# 13F-Reporter
Creates an empty excel workbook and appends two dataframes as separate sheets: one from a list of SEC 13F Securities, and another from an in-house data table containing FCM Positions information. Once the workbook is created, the program then joins the two dataframes based on matching CUSIPs.

To use 13F Reporter with an SEC 13F PDF that you want to scrape data from:
- place the 13F PDF file into the root directory (containing main.py)
- double click main.exe to launch
- when prompted to open a file, select the 13F PDF from your directory
- when prompted to save a file, choose any name to give the Excel workbook, and save

Notes:
- this version relies on free-to-use (which is advertised on their youtube tags at: https://www.youtube.com/watch?v=4AFepZ8L7xw&t=128s) code from the3dubs, found at https://github.com/the3dubs/13F-PDF-Converter
- the current 13F PDF is an example PDF - replace it with any 13F PDF you wish
