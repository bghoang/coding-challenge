'''
Bao Hoang
This is the main file for the passwd parsing  
'''
import sys
import json
import os

ARGV_ONE = 1
ARGV_TWO = 2
CORRECT_ARG_LEN = 3
WRONG_ARG_LEN = 2
INDENT = 4
USERID = "uid"
FULL_NAME = "full_name"
GROUPS = "groups"

''' 
This is the main function of this file
It will check if the user put in the correct argument 
It will print out the final result of the dictionary
'''

def main():
	# Show the usage if user put in help
	if sys.argv[ARGV_ONE] == "--help" and len(sys.argv) == WRONG_ARG_LEN:
		print("	Usage: python main.py [PATH1] [PATH2]")
		print("	PATH1: path to etc/passwd")
		print("	PATH2: path to etc/group")
		exit()
	# Check if user pass in the correct amount of arg
	if len(sys.argv) != CORRECT_ARG_LEN:
		print("	Must only pass in path to etc/passwd and etc/group")
		print("	Try 'python main.py --help' for usage instruction")
		exit()
	
	else:
		# Getting the path from the user
		passwdPath = sys.argv[ARGV_ONE]
		groupPath = sys.argv[ARGV_TWO]
		
		# Try opening the file from the given paths
		try:
			# Open the etc/passwd files	
			passwdFile = open(passwdPath, "r")
			# Open the etc/group files
			groupFile = open(groupPath, "r")
		except IOError: 
			print("	Cannot open files, please check your path again")
			print("	Try 'python main.py --help' for usage instruction")
			exit()

		# Create an empty dict
		userDict = {}
		# Read the /etc/passwd files and update userDict
		userDict = readPasswdFile(passwdFile, userDict)
	
		# Read the /etc/group files and update userDict	
		userDict= readGroupFile(groupFile, userDict)
		
		# Convert dict to json object
		userDict = json.dumps(userDict,indent=INDENT)
		print(userDict)

''' 
This function to read the files in etc/passwd
It takes in 2 parameters, first one is the file and the second one is a dictionary
This function will return a dictionary that has been updated
''' 		
def readPasswdFile(passwdFile, newDict):
	# Start reading the file
	eachLine = passwdFile.readline()
	# Read each line of the files
	while eachLine:
		# Get username from each line
		UserName = eachLine.split(':')[0]
		# Get user ID from each line 
		userID = eachLine.split(':')[2]
		# Get full name for each line
		userInfo = eachLine.split(':')[4]
		# Initiate a new username with its user ID and full name
		newDict[UserName] ={}
		# Add user ID to the dict
		newDict[UserName][USERID] = userID 
		# Add full name to the list
		newDict[UserName][FULL_NAME] = userInfo
		# Initiate an empty group array
		newDict[UserName][GROUPS] = []
		# Move to the next line 
		eachLine = passwdFile.readline()
	passwdFile.close()
	return newDict
 
'''
This function to read the file in the etc/group
It takes in 2 parameters, the first one is the file that contain all the file
in etc/group and the second on is a dictionary
The method will return a dictionary
''' 
def readGroupFile(groupFile, newDict):
	# Read the file line by line
	line = groupFile.readline()
	while line:
		# Get the group name
		groupName = line.split(':')[0]
		# Get each user in the same group
		groupList = line.split(':')[3].split(',')
		# Loop throught the list containing user name
		for name in groupList:
			# Check if the user name match those in the dict
			if name in newDict:
				# If yes then add it to the groups list in the dict
				newDict[name][GROUPS].append(groupName.rstrip('\n'))
		# Move to next line
		line = groupFile.readline()
	groupFile.close()
	return newDict
		
if __name__ == "__main__":
	main()
