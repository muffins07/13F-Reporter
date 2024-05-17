# 13f-scraper
This iteration creates an empty excel file and populates it with information from a 13F Securities PDF. It then formats the CUSIP column to contain no whitespace.

To use 13f scraper with a 13F file that you want to scrape data from:
- place the 13F PDF file into any directory containing: init_workbook.py, main.exe, pdf_converter.py, remove_white_space.py
- double click main.exe to launch
- when prompted to open a file, select the 13F PDF from your directory
- when prompted to save a file, select the newly-created "test" file in your directory and click save; if you are asked to replace it, select "yes"
- this will produce a "test (no whitespace)" file, which is the formatted (at least in the CUSIP column) and converted excel file of the 13f PDF

Notes:
- the main.exe is the distributable version, so there aren't any dependencies that should be needed to run it.
- this version relies on free-to-use (which is advertised on their youtube tags at: https://www.youtube.com/watch?v=4AFepZ8L7xw&t=128s) code from the3dubs, found at https://github.com/the3dubs/13F-PDF-Converter
- the current 13F PDF is an example PDF - replace it with any 13F PDF you wish
