"""SMS Bulk

This program will help you to send mass SMS to a bunch of cell number store in CSV file
"""

import sys
import argparse
import csv
import gammu

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

def get_cellnumbers(file):
    """Get cell numbers from CSV file
    
    Parameters:
        file: csv file
    
    Returns:
        list: list of cell numbers
    """
    list = []
    with open(file) as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        for row in reader:
            list.append(row[0])
    return list
            
def send(text, list_of_cellnum):
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

parser = argparse.ArgumentParser(description='Send SMS to bulk cell number using list of cell numbers store in CSV file')
parser.add_argument("TEXT_CONTENT", help="text content")
parser.add_argument("CSV_PATH", help="csv file which contain list of cellnumber, no column header please !!!")
args = parser.parse_args()

list_cellnum = get_cellnumbers(args.CSV_PATH)
send(args.TEXT_CONTENT, list_cellnum)