import json
import csv
from sys import argv


first = str(argv[1])
if '.json' not in first:
    first += '.json'
with open(first) as input_file:
    json_content = input_file.read()
data = json.loads(json_content)
output_file_name = list(data.keys())[0]
with open(output_file_name+'.csv', 'w') as output_file:
    fieldnames = list(data[output_file_name][0].keys())
    write_csv_keys = csv.writer(output_file, delimiter=';', lineterminator='\n')
    write_csv_keys.writerow(fieldnames)
    write_csv = csv.DictWriter(output_file, fieldnames=fieldnames, delimiter=';', lineterminator='\n')
    write_csv.writerows(data[output_file_name])
