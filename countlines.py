# tool: countlines
# number of required args: 1
# help: count the lines in a text file. /r/n First argument is the text file name.

import os

def run(args):
	file = args[0]

	print("# of lines in " + file)

	lineCnt = 0
	
	if os.path.isfile(file) == False:
		print ("File does not exist")
	else:
		with open(file, 'r') as f:
			for line in f:
				lineCnt += 1
		print(lineCnt)