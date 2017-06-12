'''
Todo: 
- figure out how to run apps from this program without having to call instance of app. 
	Use a function as parameter? So I can just call run?
- use CMD library to create interactive terminal

'''

import sys
sys.path.insert(0, 'c:/py/myTools')

import os


app = ""
appArgs = ""
apps = []
appIndex = 0

class tool:
	def __init__(self, argName, numArgs, helpMessage):
		self.name = argName
		self.numberOfReqArgs = numArgs
		self.helpMsg = helpMessage

	def displayHelp(self):
		print(self.helpMsg)

	def isThereEnoughArgs(self, args):
		if (len(args) < self.numberOfReqArgs):
			print("Not enough arguments")
			return False
		else:
			return True	

def init():
	print("")
	apps.append(tool("countlines", 1, "first argument is the text file name"))
	# go through .py files in folder, read top line comments, get out the arguments needed to instantiate the tools.

def parseArgsFromCommandPrompt():
	global app
	global appArgs 

	# get all arguments
	args = sys.argv
	del args[0] # remove the .py element
	
	# get the tool
	findAppIndex(args[0])
	app = args[appIndex]
	app = app.lower()

	# get the args for the tool
	del args[0]
	appArgs = args

def parseArgs(args):
	global app
	global appArgs

	# get the tool
	findAppIndex(args[0])
	if (appIndex > -1):
		app = args[appIndex]
		app = app.lower()	

		# get the args for the tool
		del args[0]
		appArgs = args
	else:
		print('Cant find app')

def findAppIndex(appName):
	global appIndex
	i = 0
	
	for a in apps:
		if a.name == app:
			appIndex = i
		i += 1

def execApp(app, args):
	global apps
	global appIndex

	#print(str(len(apps)))
	
	myTool = apps[appIndex]
	
	#print(myTool.name)
	if(myTool.isThereEnoughArgs(args) == False):
		print("TESTING")
## TODO CAN I EXECUTE THE PROGRAM USING myTool ??? Can I put a reference to a module or import or function as object in class


	if (app == "countlines"):
		countlines = tool("countlines", 1, "first argument is the text file name")
		if (countlines.isThereEnoughArgs(args) == False):
			return

		import countlines
		countlines.run(args)
	elif(app == "lalala"):
		print("lalala not implemented")
	else:
		print("tool doesn't exist")

def displayApps():
	global apps

	print("Tools:")
	
	for a in apps:
		print("   " + a.name)

def run():
	global app
	global appArgs 
	
	init()
	
    # make interactive prompt here
	while True:
		n = input(">>")   
		if n  == 'exit' :
			break;
		elif n == 'help':
			displayApps()
		else:
			parseArgs(n.split(" ")) # get the app and arguments
			execApp(app, appArgs) # execute the app

	#parseArgs() # get the app and arguments
	#execApp(app, appArgs) # execute the app

if __name__ == "__main__":
	run()
