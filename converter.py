import json
import csv
import argparse
import sys
import codecs

from urllib.request import urlopen
from urllib.error import URLError
from json.decoder import JSONDecodeError

class File:
	def __init__(self, url=None, file=None):
		self.url = url
		self.file = file
		self.codecs_reader = codecs.getreader('utf-8')

	def __enter__(self):
		if self.file:
			try:
				self.reader = open(self.file, 'r')
			except OSError:
				print('[*] Invalid file path! Exiting')
				sys.exit()
			except FileNotFoundError:
				print('[*] File not found! Exiting')
				sys.exit()

		elif self.url:
			try:
				self.reader = self.codecs_reader(urlopen(self.url))
			except ValueError:
				print('[*] URL not valid! Exiting')
				sys.exit()
			except URLError:
				print('[*] Invalid URL or there is a network problem! Exiting')
				sys.exit()
		else:
			print('[*] You must pass either a file-path or URL to File class! Exiting')
			sys.exit()
		
		return self.reader

	def __exit__(self, exc_type, exc_value, traceback):
		self.reader.close()


def json_to_csv(jsonfile):
	with open('output.csv', 'w', newline='') as csvfile:
		jsn = json.load(jsonfile)

		fieldnames = []
		for name in jsn[0]:
			fieldnames += [name]
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

		writer.writeheader()
		for elem in jsn:
			writer.writerow(elem)

def csv_to_json(csvfile):
	with open('output.json', 'w') as jsonfile:
		reader = csv.DictReader(csvfile)
		jsn = []
		for row in reader:
			jsn += [row]

		if not jsn:
			print('[*] Input file is blank or not a valid CSV file! Exiting')
			sys.exit()

		json.dump(jsn, jsonfile)

def convert(filetype, file):
	if (filetype=='csv'):
		csv_to_json(file)
		return ('json')
	elif (filetype=='json'):
		json_to_csv(file)
		return ('csv')

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('inputtype', help='The type of input', type=str, choices=['csv', 'json'])
	parser.add_argument('filepath', help='Path or URL of the input file', type=str)
	parser.add_argument('-f', '--file', help='If filepath is a local file path', action='store_true')
	parser.add_argument('-u', '--url', help='If filepath is an URL', action='store_true')
	args = parser.parse_args()

	try:
		if args.file:
			with File(file=args.filepath) as file:
				outputtype = convert(filetype=args.inputtype, file=file)
		elif args.url:
			with File(url=args.filepath) as file:
				outputtype = convert(filetype=args.inputtype, file=file)
		else:
			with File(file=args.filepath) as file:
				outputtype = convert(filetype=args.inputtype, file=file)
	except JSONDecodeError:
		print('[*] Input file is not a valid JSON file! Exiting')
		sys.exit()

	print('[*] Output saved as output.{}'.format(outputtype))


if __name__=='__main__':
	main()