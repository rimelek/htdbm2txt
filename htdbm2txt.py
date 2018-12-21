import dbm
import argparse
import shutil
import os
import sys

parser = argparse.ArgumentParser(description='Convert rewritemap dbm file back to txt file')
parser.add_argument('-i', dest='input', help='Input file (dbm)')
parser.add_argument('-o', dest='output', help='Output file (txt)')

args = parser.parse_args()

inputPath = args.input
outputPath = args.output
inputPathTemp = args.input + '.db'

if not os.path.isfile(inputPath):
    print(inputPath + ' does not exist', file=sys.stderr)
    sys.exit(1)

if os.path.exists(inputPathTemp):
    print(inputPathTemp + ' already exists. Delete it and try again.')
    sys.exit(1)

if os.path.exists(outputPath):
    print(outputPath + ' already exists. Delete it and try again.')
    sys.exit(1)


shutil.copy(inputPath, inputPathTemp)

# This actually open inputPathTemp because the extension appended automatically
db = dbm.open(inputPath, 'r')

keys = db.keys()

txt = open(outputPath, 'x')

for key in keys:
    line = key + b' ' + db[key] + b"\n"
    txt.write(line.decode('utf-8'))

txt.close()
db.close()

os.remove(inputPathTemp)


