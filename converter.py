import json
import csv

def json_to_csv(json_file):
	with open(json_file, 'r') as jsonfile, open('output.csv', 'w', newline='') as csvfile:
		jsn = json.load(jsonfile)
		fieldnames = []
		for name in jsn[0]:
			fieldnames += [name]
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

		writer.writeheader()
		for elem in jsn:
			writer.writerow(elem)

filename = input('Enter filename of JSON file: ')
json_to_csv(filename)