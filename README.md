# Automate boring stuff on sending SMS (Windows)

## Preparing Gammu
1. Install [Python 3.6](https://www.python.org/downloads/windows/) 64 bit for Windows
2. Install [Gammu](https://dl.cihar.com/gammu/releases/windows/Gammu-1.39.0-Windows-64bit.exe) binaries 64 bit
3. Install [python-gammu](https://dl.cihar.com/python-gammu/win32/python-gammu-2.11.win-amd64-py3.6.exe) binaries version with python 3.6 support
4. Install [driver](http://www.totalcardiagnostics.com/support/Knowledgebase/Article/View/92/20/prolific-usb-to-serial-fix-official-solution-to-code-10-error)
5. Plug the modem (I use Wavecom Fastrack M1306B)
6. Create file named gammurc on current directory

## How to create gammurc
Create plain text file (no extension) in the same directory of this python script. Write this configuration script on gammurc file:
```text
[gammu]
device=com4
connection=at115200
```
`device=com4` is device location, it can be com5 or com3, that depends on which port you plug your modem on the PC.
`connection=at115200`, just keep it as it is (tested for Wavecom Fastrack M1306B)

## How to use
Massive SMS

```text
usage: smsbulk.py [-h] TEXT_CONTENT CSV_PATH

Send SMS to bulk cell number using list of cell numbers store in CSV file

positional arguments:
  TEXT_CONTENT  text content
  CSV_PATH      csv file which contain list of cellnumber, no column header
                please !!!

optional arguments:
  -h, --help    show this help message and exit
```

Single SMS
```text
usage: smsone.py [-h] TEXT_CONTENT CELL_NUMBER

Send single SMS

positional arguments:
  TEXT_CONTENT  text content
  CELL_NUMBER   cell number

optional arguments:
  -h, --help    show this help message and exit
```

## TODO
- inbox