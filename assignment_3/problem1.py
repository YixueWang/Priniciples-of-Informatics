# Functions for students to implement.
def solveOnlyLists(inputList):
    uniqueList = []
    for i in inputList:
    	if not i in uniqueList:
    		uniqueList.append(i)
    #compute unique items in inputList
    return uniqueList

def solveDict(inputList):
    uniqueList = []
    d = {}
    uniqueList = d.fromkeys(inputList).keys()
    #compute unique items in inputList
    return uniqueList

def solveSorted(sortedInputList):
    uniqueList = []
    d = sortedInputList[0]
    for item in sortedInputList:
        if d == item:
            pass
        else:
            uniqueList.append(item)
            d = item
    ##compute unique items in inputList
    return uniqueList
