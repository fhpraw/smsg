# Automate boring stuff like sending massive SMS (on Windows)

This is a simple program for sending mass SMS.

## Preparing Gammu
1. Install [Python 3.6](https://www.python.org/downloads/windows/) 64 bit for Windows
2. Install [Gammu](https://dl.cihar.com/gammu/releases/windows/Gammu-1.39.0-Windows-64bit.exe) binaries 64 bit
3. Install [python-gammu](https://dl.cihar.com/python-gammu/win32/python-gammu-2.11.win-amd64-py3.6.exe) binaries version with python 3.6 support
4. Install [driver](http://www.totalcardiagnostics.com/support/Knowledgebase/Article/View/92/20/prolific-usb-to-serial-fix-official-solution-to-code-10-error)
5. Plug the modem (I use Wavecom Fastrack M1306B)
6. Create file named gammurc on current directory

## How to use
Massive SMS

```sh
usage: smsbulk.py [-h] TEXT_CONTENT XLSX_PATH SHEET_NAME COLUMN_LOCATION

positional arguments:
  TEXT_CONTENT     text content
  XLSX_PATH        xlsx file which contain list of cellnumber
  SHEET_NAME       active sheet name in xlsx file
  COLUMN_LOCATION  column location in active sheet

optional arguments:
  -h, --help       show this help message and exit
```

## TODO
- add CSV support
- single SMS support
- set gammurc file