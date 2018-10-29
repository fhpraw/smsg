import smsg
import argparse

def sendthem(text_content, xlsx_path, sheet_name, column_location, use_header):
    list_cellnum = smsg.get_column_values(xlsx_path, sheet_name, column_location, use_header)
    smsg.send_bulk_message(text_content, list_cellnum)

parser = argparse.ArgumentParser()
parser.add_argument("TEXT_CONTENT", help="text content")
parser.add_argument("XLSX_PATH", help="xlsx file which contain list of cellnumber")
parser.add_argument("SHEET_NAME", help="active sheet name in xlsx file")
parser.add_argument("COLUMN_LOCATION", help="column location in active sheet")
parser.add_argument("--noheader", action="store_true", help="with no header on column")
args = parser.parse_args()

if args.noheader:
    sendthem(args.TEXT_CONTENT, args.XLSX_PATH, args.SHEET_NAME, args.COLUMN_LOCATION, False)
else:
    sendthem(args.TEXT_CONTENT, args.XLSX_PATH, args.SHEET_NAME, args.COLUMN_LOCATION, True)