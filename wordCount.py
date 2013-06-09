# The object of this application is to take a string of words, 
# count the instances of each word, 
# and sort them according to the number of instances most to least


####
#### REBUILD ALL! Use Dictionary to keep track of things, i.e. [word]->[wordcount]
####

inputListOfWords = 'hej, ost, med, dig, ost'
wordDictionary = {}

def buildDictionary(wordList):
	tmpDict = {}	
	wordStringArray = wordList.split(',')
	for item in wordStringArray:
# FIX:		tmpDict.update({item,0})
	return tmpDict

def showInput(inputString):
	print ('Input: ' + inputString)

#--- RUNABLE ---#

showInput(inputListOfWords)
wordDictionary = buildDictionary(inputListOfWords)
