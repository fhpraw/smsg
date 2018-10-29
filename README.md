# Simple SMS cli (on Windows)

This is a simple program for sending mass SMS.

## Preparing Gammu
1. Install [Python 3.6](https://www.python.org/downloads/windows/) 64 bit for Windows
2. Install [Gammu](https://dl.cihar.com/gammu/releases/windows/Gammu-1.39.0-Windows-64bit.exe) binaries 64 bit
3. Install [python-gammu](https://dl.cihar.com/python-gammu/win32/python-gammu-2.11.win-amd64-py3.6.exe) binaries version with python 3.6 support
4. Install python binding
    ```sh
    pipenv install python-gammu 
    ```
5. Install [driver](http://www.totalcardiagnostics.com/support/Knowledgebase/Article/View/92/20/prolific-usb-to-serial-fix-official-solution-to-code-10-error)
6. Install modem (wavecom facetrack)
