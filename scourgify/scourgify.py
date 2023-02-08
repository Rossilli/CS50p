import csv
import sys
import os

if len(sys.argv) != 3 or not sys.argv[1].endswith('.csv'):
    sys.exit("Invalid")

input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.isfile(input_file) or not os.access(input_file, os.R_OK):
    sys.exit("Invalid")

with open(input_file, 'r') as input_csv, open(output_file, 'w', newline='') as output_csv:
    reader = csv.DictReader(input_csv)
    writer = csv.writer(output_csv)
    writer.writerow(["first", "last", "house"])
    for row in reader:
        names = row['name']
        house = row['house']
        names = names.replace('"', '')
        names = names.split(', ')
        first = names[1]
        last = names[0]
        writer.writerow([first, last, house])