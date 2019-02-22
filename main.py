'''
Bao Hoang
This is the main file for the passwd parsing  
'''
import sys
import json
import os

def main(*args, **kwargs):
	# Show the usage if user put in help
	if sys.argv[1] == "--help" and len(sys.argv) == 1:
		print("Usage: python main.py [PATH1] [PATH2]")
		print("PATH1: path to etc/passwd")
		print("PATH2: path to etc/group")
		exit()
	# Check if user pass in the correct amount of arg
	if len(sys.argv) != 2:
		print("Must pass in path to etc/passwd and etc/group")
		print("Try '--help' for usage instruction")
		exit()
	
	else:
		# Getting the path from the user
		passwdPath = sys.argv[1]
		groupPath = sys.argv[2]

		userDict = {}
		# Read the /etc/passwd files and update userDict
		userDict = readPasswdFile(passwdPath, userDict)
	
		# Read the /etc/group files and update userDict	
		userDict= readGroupFile(groupPath, userDict)
		
		# Convert dict to json object
		userDict = json.dumps(userDict,indent=4)
		print(userDict)

 		
def readPasswdFile(passwdPath, newDict):
	# Open the etc/passwd files	
	passwdFile = open(passwdPath, "r")
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
		newDict[UserName]["uid"] = userID 
		# Add full name to the list
		newDict[UserName]["full_name"] = userInfo
		# Initiate an empty group array
		newDict[UserName]["groups"] = []
		# Move to the next line 
		eachLine = passwdFile.readline()
	passwdFile.close()
	return newDict
 
def readGroupFile(groupPath, newDict):
	# Open the etc/group files
	groupFile = open(groupPath, "r")
	# Read the file line by line
	line = groupFile.readline()
	while line:
		groupName = line.split(':')[0]
		#print(groupName)
		groupList = line.split(':')[3].split(',')
		#print("list",groupList)
		for name in groupList:
			if name in newDict:
				newDict[name]["group"].append(groupName.rstrip('\n'))
				#print("name", name)
		line = groupFile.readline()
	groupFile.close()
	# Loop through the array that contain all the usernames in a group
	#newDict = json.dumps(newDict,indent=4)
	#print(newDict)
	return newDict

if __name__ == "__main__":
	main()
