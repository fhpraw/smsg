import gammu
import sys
import re
import openpyxl

DEFAULT_SHEETNAME = 'Sheet1'

def clean_all_whitespace(string):
    """Clean all white space

    Args:
        string: string
    return:
        clean string without whitespace
    """
    return re.sub(r"\s+",
                  "",
                  string,
                  flags=re.UNICODE)

def get_column_values(file_path,
                      sheet_name,
                      column_location):
    """Get all cell values from define column

    Args:
        file_path: file path
        sheet_name: sheet name
        column_location: column location
        use_header: True if using header, false if not
    Returns:
        list of values
    """

    # create empty list for storing cell value
    list_col_value = []

    try:
        # load excel file
        wb = openpyxl.load_workbook(file_path)
    except FileNotFoundError:
        # file not found or wrong file path
        sys.exit('Wrong file or file path')

    # choose active sheet
    sheet = wb[sheet_name]

    # get cell value from defined column location
    for cell in sheet[column_location]:
        list_col_value.append(cell.value)

    # return
    return list_col_value

def get_all_values(filename, sheetname):
    """ get all values from excel file

    Args:
        filename: excel file
        sheetname: sheet name
    Returns:
        list of values
    """
    list_all_value = []
    wb = openpyxl.load_workbook(filename, read_only=True)
    ws = wb[sheetname]

    for row in ws.rows:
        list_all_value.append([x.value for x in row])

    return list_all_value

def define_message(text, cellnumber):
    """Create SMS message format in gammu

    Args:
        text: message
        cellnumber: cell number
    Returns:
        SMS message format in gammu

    """
    if len(text) >= 160 :
        return sys.exit('text is more than 160 characters. It is not allowed')
    else:
        message = {
            'Text': text,
            'SMSC': {'Location': 1},
            'Number': cellnumber,
        }
        return message

def send_bulk_message(text, list_of_cellnumber):
    """Send mass SMS to multiple cell number

    Args:
        text: text message
        list_of_cellnumber: list of cell number
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
    total_cellnumber = len(list_of_cellnumber)

    for cellnumber in list_of_cellnumber:
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

print(get_all_values('sample.xlsx', DEFAULT_SHEETNAME))