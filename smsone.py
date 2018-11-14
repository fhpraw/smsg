import argparse
import smsg

parser = argparse.ArgumentParser(description='Send single SMS')
parser.add_argument("TEXT_CONTENT", help="text content")
parser.add_argument("CELL_NUMBER", help="cell number")
args = parser.parse_args()

smsg.send_one(args.TEXT_CONTENT, args.CELL_NUMBER)