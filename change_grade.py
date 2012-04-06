#!/usr/bin/env python

import re
import fileinput
from sys import stderr,stdout,argv,exit

def changeGrade(name,newGrade):
	lines = ""
	for line in fileinput.input('-'):
		m = re.search(name,line)
		if m:
			newline = re.sub(r'\d+',newGrade,line)
			lines += newline
		else:
			lines += line
	return lines



if __name__=='__main__':
	 
	if len(argv) != 3:
		stderr.write("Usage: change_grade.py STRING INTEGER\n")
		exit(1)
	else:
		lines = changeGrade(argv[1],argv[2])
		print lines
	
	










