'''
Bao Hoang
This is the main file for the passwd parsing  
'''
import sys
import json
from collections import OrderedDict
#import collections
import os


def main():
	# Getting the path from the user
	passwdPath = sys.argv[1]
	groupPath = sys.argv[2]
	# Read the /etc/passwd files
	readPasswdFile(passwdPath)
	# Read the /etc/group files	
	'''groupFile = open(groupPath, "r")
	line = groupFile.readline()
	while line:
		print(line)
		line = groupFile.readline()
	groupFile.close()
'''
	#print(passwdFile)
	#print(groupPath)

def readPasswdFile(passwdPath):
	newDict = {}
	passwdFile = open(passwdPath, "r")
	eachLine = passwdFile.readline()
	while eachLine:
		#print(eachLine)
		UserName = eachLine.split(':')[0] 
		userID = eachLine.split(':')[2]
		userInfo = eachLine.split(':')[4]
		newDict[UserName] = {"uid": userID, "full_name": userInfo, "group": []}
		#newDict.update(UserName={{"group": [],"uid": userID, "full_name": userInfo}})
		eachLine = passwdFile.readline()
	passwdFile.close()
	newDict = sorted(newDict, reverse=True)
	#newDict = collections.OrderedDict(newDict)
	# Convert dict to string object
	newDict = json.dumps(newDict,indent=4)
	# Convert dict to json file
	#newDict = json.loads(newDict)
	print(newDict)
 

if __name__ == "__main__":
	main()
