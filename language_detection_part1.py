# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 14:34:10 2022

@author: raksha
"""


def openFilewithReadAccess(fileName, fileEncoding):
    try:
        file = open(fileName, 'r', encoding=fileEncoding)
        return file
    except FileNotFoundError:
        return None

def readStringFromFile(myFile):
    return myFile.read()

def makeAllCharactersLowerCase(myString):
    resString = myString.lower()
    return resString

def parseStringAndCreateCharacterFrequencyDict(myString):
    resDict = {}
    for i in myString:
        if (i.isalpha()):
            if i in resDict:
                resDict[i] += 1
            else:
                resDict[i] = 1
    return resDict


def getSortedLetterFrequencyFingerPrint(myString):
    resDict = parseStringAndCreateCharacterFrequencyDict(myString)
    # item = ('a', 200), so item[0] = 'a' and item[1] = 200
    # softing dictionary based on value i.e. item[1]
    sortedDict = dict(sorted(resDict.items(), key = lambda item: item[1], reverse=True))
    resList = list(sortedDict.keys())
    resString = "".join(resList)
    print(resString)
    return resString



file_a = openFilewithReadAccess("english-text.txt", "utf8")
if (file_a != None):
    s = readStringFromFile(file_a)
    s = makeAllCharactersLowerCase(s)
    getSortedLetterFrequencyFingerPrint(s)