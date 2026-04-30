#! Ideally this project will be based
#* about a dictionary that has dictionaries in itself

from configparser import ConfigParser
from Topic import Topic


def printValues(bigDict: dict):

	for value in bigDict:
		print("Values in order: ")
		print(bigDict[value])

# index of the dictionary of dictionaries
index = 0

bigDict = {}

sampleDict = {"pesce": "eccoci"}

i = 0

while i < 5:
	newTopic = Topic()

	bigDict[index] = newTopic.valueX, newTopic.valueY, newTopic.valueZ
	index += 1
	i += 1


printValues(bigDict)

# so to do it right
