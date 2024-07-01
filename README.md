# 13F-Reporter
Generates a list of securities (owned by FCM) in a file called "Information Table" to make a quarterly 13F report to the SEC.

To use software with an SEC 13F PDF from the most recent quarter:
- download the scripts from this project into one folder
- place the 13F PDF into this folder
- open & activate a virtual environment in that folder's directory, and
- download all required dependencies. Then, run "python merge.py."
- When prompted to open a file, select the 13F PDF from your directory and
- when prompted to save a file, type "fcm", and save.

Notes:
- this version relies on free-to-use code from the3dubs, found at https://github.com/the3dubs/13F-PDF-Converter; they specified that this code is free to use on their video tags.
- the current 13F PDF is an example PDF - replace it with any 13F PDF you wish.
