# The object of this application is to take a string of words, 
# count the instances of each word, 
# and sort them according to the number of instances most to least


####
#### REBUILD ALL! Use Dictionary to keep track of things, i.e. [word]->[wordcount]
####

inputListOfWords = 'hej,med,dig,ost,ost'
wordDictionary = {}

def buildDictionary(wordList):
	tmpDict = {}	
	wordStringArray = wordList.split(',')
	for item in wordStringArray:
		if(tmpDict.has_key(item)):
			newValue = tmpDict[item] + 1
			tmpDict[item] = newValue
		else:
			tmpDict.update({item:1})
		print("Key: " + item)
		print("Value: " + str(tmpDict[item]))
#	return tmpDict

def showInput(inputString):
	print ('Input: ' + inputString)

#--- RUNABLE ---#

showInput(inputListOfWords)
buildDictionary(inputListOfWords)
