import json
import csv
import argparse
import sys

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

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('inputtype', help='The type of input', type=str, choices=['csv', 'json'])
	parser.add_argument('filename', help='Name of the input file', type=str)
	args = parser.parse_args()

	if (args.inputtype=='csv'):
		try:
			csv_to_json(args.filename)
		except FileNotFoundError:
			print('[*] File not found! Exiting')
			sys.exit()
		outputtype = 'json'
	
	elif (args.inputtype=='json'):
		try:
			json_to_csv(args.filename)
		except FileNotFoundError:
			print('[*] File not found! Exiting')
			sys.exit()

		outputtype = 'csv'

	print('[*] Output saved as output.{}'.format(outputtype))


if __name__=='__main__':
	main()