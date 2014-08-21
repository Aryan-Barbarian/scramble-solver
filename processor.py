import json;
import os.path
import re
import time 

start = time.time()

filenames = []
#load books
with open("./books/books.json", "r") as infile:
	bookInfo = json.loads(infile.read())
	for key,book in bookInfo.items():
		filenames.append(book["filename"])



processedSoFar = dict()
firstThreeLetters = False;

wordsInMemory = 0;

def sortLetters(word):
	return ''.join(sorted(word))

def firstLetters(word):
	currFirstThreeLetters = sortedWord[: min(3,len(word))]
	return currFirstThreeLetters

def persistToFile(info):
	start = time.time()
	for letters,infoForLetters in info.items():
		persistLetterGroupToFile(infoForLetters,letters)
	end = time.time()
	print("IT TOOK: " + str((end - start)) + " S TO WRITE FILE")

def persistLetterGroupToFile(info,firstLetters):
	infoSoFar = dict()
	filename = str(firstLetters) + ".json"

	if os.path.isfile("./processed_scrambles/" + filename):
		with open("./processed_scrambles/" + filename, "r") as infile:
			infoSoFar = json.loads(infile.read())

	for key, name in info.items():
		if key in infoSoFar:
			infoSoFar[key] = list(set(info[key] + infoSoFar[key]))
		else:
			infoSoFar[key] = info[key]

	with open("./processed_scrambles/" + filename, "w") as outfile:
		json.dump(infoSoFar, outfile, indent=4, sort_keys = True)

	
	

for fileName in filenames:
	print(fileName)
	for line in open("./books/" + fileName):
		words = line.split(" ");
		
		for word in words:
			wordsInMemory += 1;
			word = re.sub('[^0-9a-zA-Z]+', '', word)
			word = word.lower()
			sortedWord = sortLetters(word)
			
			firstThreeLetters = firstLetters(word)			

			if firstThreeLetters not in processedSoFar:
				processedSoFar[firstThreeLetters] = dict()

			if sortedWord not in processedSoFar[firstThreeLetters]:
				processedSoFar[firstThreeLetters][sortedWord] = []
			processedSoFar[firstThreeLetters][sortedWord].append(word)

			if wordsInMemory>30000:
				persistToFile(processedSoFar);
				wordsInMemory = 0
				print("PERSIST")


end = time.time()
print("IT TOOK: " + str((end - start)) + " S")