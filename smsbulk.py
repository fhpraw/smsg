"""SMS Bulk

This program will help you to send mass SMS to a bunch of cell number store in CSV file
"""

import argparse
import smsg

parser = argparse.ArgumentParser(description='Send SMS to bulk cell number using list of cell numbers store in CSV file')
parser.add_argument("TEXT_CONTENT", help="text content")
parser.add_argument("CSV_PATH", help="csv file which contain list of cellnumber, no column header please !!!")
args = parser.parse_args()

smsg.send_bulk(args.TEXT_CONTENT, smsg.get_cellnumbers(args.CSV_PATH))