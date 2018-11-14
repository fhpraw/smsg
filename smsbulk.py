"""SMS Bulk

This program will help you to send mass SMS to a bunch of cell number store in XLSX file
"""

import sys
import argparse
import gammu
import openpyxl

def get_column_values(file, sheet, column):
    """Get all cell values from define column

    Parameters:
        file (str): The file location of the spreadsheet XLSX
        sheet (str): Active sheet name
        column (str): Column address
    
    Returns:
        list: a list of cell value based on defined column address
    """
    list = []
    try:
        # load excel file
        wb = openpyxl.load_workbook(file)
    except FileNotFoundError:
        # file not found
        sys.exit('File not found')

    # choose active sheet
    sheet = wb[sheet]

    # get cell value
    for cell in sheet[column]:
        list.append(cell.value)

    return list

def define_message(text, cellnum):
    """Create SMS message format in gammu

    Parameters:
        text (str): text message
        cellnum (str): cell number
    
    Returns:
        message: SMS message format based on gammu
    
    """
    if len(text) >= 160 :
        return sys.exit('text is more than 160 characters')
    else:
        message = {
            'Text': text,
            'SMSC': {'Location': 1},
            'Number': cellnum,
        }
        return message

def send_bulk_message(text, list_of_cellnum):
    """Send mass SMS to multiple cell number

    Parameters:
        text (str): text message
        list_of_cellnum: list of cell number
    
    Returns:
        none
    """

    # create object for talking with phone
    sm = gammu.StateMachine()

    # read gammurc configuration
    sm.ReadConfig()

    # connect to the phone
    sm.Init()

    # get total cellnumber
    total_cellnumber = len(list_of_cellnum)

    for cellnumber in list_of_cellnum:
        print(f'{total_cellnumber} cell numbers to go')
        print(f'Sending SMS to {cellnumber}...')
        try:
            sm.SendSMS(define_message(text, cellnumber))
        except gammu.GSMError:
            print(f'SMS for {cellnumber} failed')
            total_cellnumber -= 1
            continue
        print(f'The message has been succesfully sent to {cellnumber}')
        total_cellnumber -= 1

parser = argparse.ArgumentParser(description='Send SMS to bulk cell number')
parser.add_argument("TEXT_CONTENT", help="text content")
parser.add_argument("XLSX_PATH", help="xlsx file which contain list of cellnumber")
parser.add_argument("SHEET_NAME", help="active sheet name in xlsx file")
parser.add_argument("COLUMN_LOCATION", help="column location in active sheet WARNING !!! WITHOUT HEADER")
args = parser.parse_args()

list_cellnum = get_column_values(args.XLSX_PATH, args.SHEET_NAME, args.COLUMN_LOCATION)
send_bulk_message(args.TEXT_CONTENT, list_cellnum)