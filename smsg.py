import sys
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

def send_one(text, cellnumber):
    """Send single SMS

    Parameters:
        text (str): text message
        cellnum (str): cell number
    
    Returns:
        none
    """
    # create object for talking with phone
    sm = gammu.StateMachine()

    # read gammurc configuration
    sm.ReadConfig()

    # connect to the phone
    sm.Init()

    try:
        sm.SendSMS(define_message(text, cellnumber))
    except gammu.GSMError:
        print(f'SMS for {cellnumber} failed')

def send_bulk(text, list_of_cellnum):
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
