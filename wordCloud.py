from operator import itemgetter
import re

inputListOfWords = 'hej, med, dig, ost, ost gedeost endda.!/ argh'
wordDictionary = {}

def buildDictionary(wordList):
	p = re.compile('[a-zA-Z0-9]+')
	print 'RegeX: ' + str(p.findall(wordList))
	tmpDict = {}	
	wordStringArray = p.findall(wordList)
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

