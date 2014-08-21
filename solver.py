import json;
import os.path
import re
import time

start = time.gmtime()
def sortLetters(word):
	return ''.join(sorted(word))

def firstLetters(word):
	currFirstThreeLetters = sortedWord[: min(3,len(word))]
	return currFirstThreeLetters

sortedWord = ""
def solve(scrambledWord):

	global sortedWord
	scrambledWord = re.sub('[^0-9a-zA-Z]+', '', scrambledWord)
	scrambledWord = scrambledWord.lower()
	sortedWord = sortLetters(scrambledWord)
	firstThree = firstLetters(sortedWord)

	filePath = "./processed_scrambles/" + firstThree + ".json"
	print(filePath)
	if os.path.isfile(filePath):
		with open(filePath, "r") as infile:
			global sortedWord;
			solutionsDict = json.loads(infile.read())
			if sortedWord in solutionsDict:
				return "IT IS: " + str(solutionsDict[sortedWord])
			else:
				return "NOT IN FILE"
	else:
		return "FILE DOES NOT EXIST"

import sys

while(True):

	line = raw_input("Scrambled?\n")
	start = time.time()
	ans = solve(line)
	end = time.time()
	print(ans + " in [ " + str((1000*(end-start))) + " ] miliseconds." )
