from operator import itemgetter

inputListOfWords = 'hej, med, dig, ost, ost gedeost endda'
wordDictionary = {}

def buildDictionary(wordList):
	tmpDict = {}	
	wordList = wordList.replace(' ', ',')
	wordList = wordList.replace(',,', ',')
	wordStringArray = wordList.split(',')
	for item in wordStringArray:
		if(tmpDict.has_key(item)):
			newValue = tmpDict[item] + 1
			tmpDict[item] = newValue
		else:
			tmpDict.update({item:1})
	return tmpDict

#--- RUNABLE ---#

wordDictionary = buildDictionary(inputListOfWords)
print('Input list of words: ' + inputListOfWords)
print('Dictionary: %s' % wordDictionary)
for key in sorted(wordDictionary, key=itemgetter(1), reverse=True):
	print('Key: ' + str(key))
	print('Value: ' + str(wordDictionary[key]))

