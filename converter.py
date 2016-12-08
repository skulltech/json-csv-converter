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

def csv_to_json(csv_file):
	with open(csv_file, 'r') as csvfile, open('output.json', 'w') as jsonfile:
		reader = csv.DictReader(csvfile)
		jsn = []
		for row in reader:
			jsn += [row]

		json.dump(jsn, jsonfile)
		
filename = input('Enter filename of CSV file: ')
csv_to_json(filename)