#! /usr/bin/python3

from pptx import Presentation

# Get user input
num_merge = int(input("Please enter the number of PPTs you want to merge: "))
fpath_1 = input("Please enter the path to the first file: ")

# Open file for reading
file_main = open(file_path)
prs_main = Presentation(open_file)

for _ in range(1, num_merge-1):
	fpath_2 = input("Please enter the path to the next file: ")
	print(fpath2)