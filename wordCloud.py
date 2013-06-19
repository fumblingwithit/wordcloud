#!/usr/bin/python
from operator import itemgetter
import re
import cgi

form = cgi.FieldStorage()

inputListOfWords = form.getfirst('wordCloudText', 'empty')
inputListOfWords = (cgi.escape(inputListOfWords)).lower()

wordDictionary = {}
listOfWordsToIgnore = ['he', 'so', 'to', 'no', 'of', 'we', 'in', 'an', 'she', 'on', 'not', 'his', 'as', 'you', 'the', 'mr', 'me', 'if', 'be', 'or', 'him', 'and']

def buildDictionary(wordList, ignoreList):
        p = re.compile('[a-zA-Z0-9]+')
        tmpDict = {}
        wordStringArray = p.findall(wordList)
        for item in wordStringArray:
		if (item not in ignoreList):
	                if(tmpDict.has_key(item)):
	                        newValue = tmpDict[item] + 1
	                        tmpDict[item] = newValue
	                else:
	                        tmpDict.update({item:1})		
        return tmpDict

#--- RUNABLE ---#

wordDictionary = buildDictionary(inputListOfWords, listOfWordsToIgnore)

print """\
Content-Type: text/html\n
<html><body>
"""

print """\
<p>The submitted text gives this list of words:</p>
"""

for key, value in sorted(wordDictionary.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    print "Key: %s &nbsp;&gt;&nbsp; Value: %s <br />\n" % (key, value)

print """\
</body></html>
"""

