inputListOfWords = 'hej, ost, med, dig, ost'
listOfWords = []

wordList1 = ['ost', 0]
wordList2 = ['hej', 0]
wordList3 = ['ost', 0]

def showInput(inputString):
	print ('Input: ' + inputString)


def buildListOfWords(wordList, newWordList):
	wordList.append(newWordList)
	return wordList

def showWordList(wordList):
	print(wordList)

#--- RUNABLE ---#

buildListOfWords(listOfWords, wordList1)
buildListOfWords(listOfWords, wordList2)
buildListOfWords(listOfWords, wordList3)

showWordList(listOfWords)
#showInput(inputListOfWords)
