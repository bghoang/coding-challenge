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
	updateDict = {}
	# Read the /etc/passwd files
	updateDict = readPasswdFile(passwdPath, updateDict)
	
	# Read the /etc/group files	
	groupArray= readGroupFile(groupPath, updateDict)
	#print(updateDict)
 		
def readPasswdFile(passwdPath, newDict):
	#newDict = {}
	passwdFile = open(passwdPath, "r")
	eachLine = passwdFile.readline()
	while eachLine:
		UserName = eachLine.split(':')[0] 
		userID = eachLine.split(':')[2]
		userInfo = eachLine.split(':')[4]
		newDict[UserName] = {"uid": userID, "full_name": userInfo, "group": []}
		#newDict.update(UserName={{"group": [],"uid": userID, "full_name": userInfo}})
		eachLine = passwdFile.readline()
	passwdFile.close()
	#newDict = sorted(newDict, reverse=True)
	#newDict = collections.OrderedDict(newDict)
	# Convert dict to string object
	#newDict = json.dumps(newDict,indent=4)
	# Convert dict to json file
	#newDict = json.loads(newDict)
	#print(newDict)
	return newDict
 
def readGroupFile(groupPath, newDict):
	groupFile = open(groupPath, "r")
	groupArray=[]
	line = groupFile.readline()
	while line:
		groupList = line.split(':')[3]
		if groupList.strip():
			groupArray.append(groupList)		
			#print(groupList)
		line = groupFile.readline()
	groupFile.close()
	for i in range(len(groupArray)):
		groupArray[i] = groupArray[i].strip('\n')
	print(groupArray)
	return groupArray	


if __name__ == "__main__":
	main()
