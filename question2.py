import sys
from pathlib import Path

def validate_files(input_files):
	if len(input_files)!=2:
		print('Invalid Input. Please enter 2 files')
	elif Path(input_files[0]) and Path(input_files[1]):
		return input_files
	else:
		if not Path(input_files[0]):
			print('invalid File:', input_files[0])
		if not Path(input_files[1]):
			print('invalid File:', input_files[1])
		sys.exit()	

def compare_files(file_1, file_2):
	file_1_strings = dict()
	with open(file_1,'r') as input_file:
		for line in input_file:
			for word in line.split():
				file_1_strings[word] = 0

	
	with open(file_2,'r') as input_file:
		for line in input_file:
			for word in line.split():
				if word in file_1_strings:
					file_1_strings[word] =1
	
	return (sum([val for key,val in file_1_strings.items()]))

def common_strings():
	file_1, file_2 = validate_files(sys.argv[1:])
	string_count = compare_files(file_1, file_2)


