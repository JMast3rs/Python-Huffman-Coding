def getFrequency(text):
    charList = []
    
    for char in text:
        if charList.count(char) == 0:
            charList += [char]
            
    charCount = []
    
    for chars in charList:
        charCount += [text.count(chars)]
    
    print(charList)
    print(charCount)
    
    return charList, charCount


def getSmallest(charList, charCount):
    smallest = min(charCount)
    for i in range(len(charCount)):
        if smallest == charCount[i]:
            return i

def removeIndex(index, list):
    return list[:index] + list[(index+1):]

def branch(charList, charCount):
    index = getSmallest(charList, charCount)
    one = [charList[index], charCount[index]]
    charList = removeIndex(index, charList)
    charCount = removeIndex(index, charCount)
    
    index = getSmallest(charList, charCount)
    two = [charList[index], charCount[index]]
    charList = removeIndex(index, charList)
    charCount = removeIndex(index, charCount)
    
    charList += [[ one[0], two[0] ]]
    charCount += [ one[1] + two[1] ]
    
    return charList, charCount

def buildTree(charList, charCount):
    while len(charList) > 2:
        charList, charCount = branch(charList, charCount)
    return charList, charCount

def searchTree(target, tree):
    if len(tree[0]) == 2:
        left = searchTree(target, tree[0])
    else:
        if tree[0] == target:
            return "0"
        else:
            return "3"
    
    if len(tree[1]) == 2:
        right = searchTree(target, tree[1])
    else:
        if tree[1] == target:
            return "1"
        else:
            return "3"
    
    if list(left).count("3") == 1:
        return "1" + right
    else:
        return "0" + left
    
        
    
    
            
            

a = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDEEEEEEEEEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFGGGGGGGGGGGGGGGGGGGGGGG"

charList, charCount = getFrequency(a)

normalList = charList

charList, charCount = buildTree(charList, charCount)

for i in normalList:
    print(i + " " + searchTree(i, charList))


print(charList)
print(charCount)
