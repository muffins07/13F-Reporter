# 13F-Reporter
Generates a list of SEC securities (owned by FCM) to report on a quarterly 13F Report.

To use software with an SEC 13F PDF from the most recent quarter:
- place the 13F PDF into a folder containing all scripts, including merge.py
- open a python terminal in that folder directory, and run "python merge.py"
- when prompted to open a file, select the 13F PDF from your directory and
- when prompted to save a file, type "fcm", and save.

Notes:
- this version relies on free-to-use code from the3dubs, found at https://github.com/the3dubs/13F-PDF-Converter; they specified that this code is free to use on their video tags.
- the current 13F PDF is an example PDF - replace it with any 13F PDF you wish.
