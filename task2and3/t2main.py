import json
from getOperatorsAndNumbes import getOperatorByCode, getUserNumber


# main function with read from file
def readFromFile():
    file = open("numbers.json", "r")
    fileData = json.load(file)
    file.close()
    for i in fileData:
        for y in fileData[i]:
            print(i, y)
    getOperatorByCode(fileData)
    getUserNumber(fileData)


readFromFile()
