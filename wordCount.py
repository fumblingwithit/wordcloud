from operator import itemgetter
# The object of this application is to take a string of words, 
# count the instances of each word, 
# and sort them according to the number of instances most to least


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
	return tmpDict

def sortDictionary(tmpDict):
	return sorted(tmpDict.items(), key=itemgetter(1), reverse=True)

def showInput(inputString):
	print ('Input: ' + inputString)


#--- RUNABLE ---#

showInput(inputListOfWords)
wordDictionary = buildDictionary(inputListOfWords)
#wordDictionary = sortDictionary(wordDictionary)
print('Dictionary: %s' % wordDictionary)
for key in sorted(wordDictionary, key=itemgetter(1), reverse=True):
	print('Key: ' + str(key))
	print('Value: ' + str(wordDictionary[key]))

