#!/usr/bin/python
from operator import itemgetter
import re
import cgi

form = cgi.FieldStorage()
inputListOfWords = form.getfirst('wordCloudText', 'empty')

# Avoid script injection escaping the user input
inputListOfWords = cgi.escape(inputListOfWords)

#inputListOfWords = 'hej, med, dig, ost, ost gedeost endda.!/ argh'
wordDictionary = {}

def buildDictionary(wordList):
	p = re.compile('[a-zA-Z0-9]+')
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

print """\
Content-Type: text/html\n
<html><body>
"""

print """\
<p>Debugging: %s</p>
""" %wordDictionary

print """\
<p>The submitted text gives this list of words:</p>
"""

sortedDictionary = sorted(wordDictionary, key=itemgetter(1), reverse=True)
for key in sortedDictionary:
	print('Key: ' + str(key) + '&nbsp;--&gt;&nbsp; Value: ' + str(wordDictionary[key]) + '<br />\n')

print """\
</body></html>
"""
