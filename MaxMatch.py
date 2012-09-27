from LexiconImprovement import LexiconImprover

__author__ = 'theraccoun'

import re

def maxMatch(inputString, dictRef):

    pointerPos = 0
    maxMatchTuple = []

    while pointerPos < len(inputString):
        longestWordInfo = findLongestWordFromPointerPos(inputString, pointerPos, dictRef, True)
        maxMatchTuple.append(longestWordInfo.get('longest_word'))
        pointerPos = longestWordInfo.get('pointer_pos')

    return maxMatchTuple

def findLongestWordFromPointerPos(string, pointerPos, dictRef, is_forward):
    longestWord = ""
    possibleWord = ""
    i = pointerPos
    if is_forward:
        while i < len(string):
            possibleWord += string[i]
            i += 1

            if possibleWord.isdigit():
                pointerPos = i
                return {'longest_word' : possibleWord, 'pointer_pos' : pointerPos}

            if dictRef.__contains__(possibleWord):
                longestWord = possibleWord
                pointerPos = i

            if longestWord == "" and i == len(string):
                pointerPos = i
                longestWord = possibleWord
    else:
        backwardWord = ""
        while i >= 0:
            backwardWord += string[i]
            possibleWord = ""
            for z in range(len(backwardWord)):
                possibleWord += backwardWord[(len(backwardWord) - 1) - z]
            i -= 1

            if possibleWord.isdigit():
                pointerPos = i
                return {'longest_word' : possibleWord, 'pointer_pos' : pointerPos}

            if dictRef.__contains__(possibleWord):
                longestWord = possibleWord
                pointerPos = i

            if longestWord == "" and i == len(string):
                pointerPos = i
                longestWord = possibleWord

    return {'longest_word' : longestWord, 'pointer_pos' : pointerPos}

def maxMatchImprovedForward(inputString, dictRef):

    pointerPos = 0
    maxMatchTuple = []

    while pointerPos < len(inputString):
        if inputString[pointerPos].isdigit():
            longestWordInfo = computeLongestNumAndUpdatePointer(inputString, pointerPos, True)
            maxMatchTuple.append(longestWordInfo.get('longest_num'))
            pointerPos = longestWordInfo.get('pointer_pos')
        else:
            longestWordInfo = findLongestWordFromPointerPos(inputString, pointerPos, dictRef, True)
            maxMatchTuple.append(longestWordInfo.get('longest_word'))
            pointerPos = longestWordInfo.get('pointer_pos')

    return maxMatchTuple

def maxMatchImprovedBackward(inputString, dictRef):

    pointerPos = len(inputString) - 1
    backwardMatch = []

    while pointerPos >= 0:
        if inputString[pointerPos].isdigit():
            longestWordInfo = computeLongestNumAndUpdatePointer(inputString, pointerPos, False)
            backwardMatch.append(longestWordInfo.get('longest_num'))
            pointerPos = longestWordInfo.get('pointer_pos')
        else:
            longestWordInfo = findLongestWordFromPointerPos(inputString, pointerPos, dictRef, False)
            backwardMatch.append(longestWordInfo.get('longest_word'))
            pointerPos = longestWordInfo.get('pointer_pos')

    maxMatchTuple = []
    for z in range(len(backwardMatch)):
         maxMatchTuple.append(backwardMatch[len(backwardMatch) - 1 - z])
    return maxMatchTuple

def computeLongestNumAndUpdatePointer(inputString, pointerPos, is_forward):
    isNum = True
    possibleNum = ""
    i = pointerPos

    if is_forward:
        while isNum and i < len(inputString):
            curChar = inputString[i]
            i += 1
            if curChar.isdigit():
                possibleNum += curChar
                pointerPos = i
                isNum = True
    else:
        backwardNum = ""
        while isNum and i >= 0:
            curChar = inputString[i]
            i -= 1
            if curChar.isdigit():
                backwardNum += curChar
                pointerPos = i
                isNum = True

        for z in range(len(backwardNum)):
            possibleNum += backwardNum[len(backwardNum) - 1 - z]

    return {'longest_num' : possibleNum , 'pointer_pos' : pointerPos}



def maxMatchImproved(inputString, dictRef):
    backward = maxMatchImprovedForward(inputString, dictRef)
    forward = maxMatchImprovedBackward(inputString, dictRef)

    longestBack = 0
    for string in backward:
        if len(string) > longestBack:
            longestBack = len(string)

    longestForward = 0
    for string in forward:
        if len(string) > longestForward:
            longestForward = len(string)

    print "forward: " , forward
    print "backward: " , backward

    #compare the length of the first and last words of the forward and backward methods
    # those that maintain better length should win
    forward_first_last = len(forward[0]) + len(forward[len(forward) - 1])
    backward_first_last = len(backward[0]) + len(backward[len(backward) - 1])
    print forward_first_last
    print backward_first_last


    num_words_long_four_in_forward = 0
    for word in forward:
        if len(word) >= 4:
            num_words_long_four_in_forward += 1

    num_words_long_four_in_backward = 0
    for word in backward:
        if len(word) >= 4:
            num_words_long_four_in_backward += 1



    if forward_first_last != backward_first_last:
        if forward_first_last > backward_first_last:
            return forward
        else:
            return backward

    if num_words_long_four_in_forward >= num_words_long_four_in_backward:
        return forward
    else:
        return backward




def runMaxMatchImprovedForward(inputString, dictRef):
    # If the entire hashTag is found in the dictionary, that's probably it, so just return it
    possibleWord = ''
    maxMatchedString = []

    at_end_of_input_string = False
    curPointer = 0
    while not at_end_of_input_string:
        if curPointer > len(inputString) - 1:
            break
        curLetter = inputString[curPointer]

        #Check if letter is a number
        reg = re.compile('[0-9]')
        if reg.match(curLetter):
            possibleWord += curLetter
            if curPointer + 1 < len(inputString):
                next_char = inputString[curPointer+1]
                if not reg.match(inputString[curPointer+1]):
                    maxMatchedString.append(possibleWord)
                    possibleWord = ''
            else:
                maxMatchedString.append(possibleWord)
                possibleWord = ''
                break
        else:
            possibleWord += curLetter
            if dictRef.__contains__(possibleWord):
                #look ahead to end of string to see if a slightly longer word can be matched
                #if so, it's the more likely word.
                another_possibility = possibleWord
                curIndex = curPointer
                dist_to_end_of_string = len(inputString) - curPointer
                for z in range(1, dist_to_end_of_string):
                    lookAhead = curIndex + z
                    another_possibility += inputString[lookAhead]
                    if dictRef.__contains__(another_possibility):
                        possibleWord = another_possibility
                        curPointer = curIndex + z


                maxMatchedString.append(possibleWord)
                possibleWord = ''
            else:
                if curPointer == len(inputString) - 1:
                    maxMatchedString.append(possibleWord)
                    break

        curPointer += 1

    if len(maxMatchedString) == 0:
        maxMatchedString = [inputString.rstrip()]
    return maxMatchedString


def runMaxMatchImprovedBackward(inputString, dictRef):
    # If the entire hashTag is found in the dictionary, that's probably it, so just return it
    possibleWord = []
    maxMatchedString = []

    behind_beginning_of_string = False
    curPointer = len(inputString) - 1
    while not behind_beginning_of_string:
        if curPointer < 0:
            break
        curLetter = inputString[curPointer]

        #Check if letter is a number
        reg = re.compile('[0-9]')
        if reg.match(curLetter):
            possibleWord.insert(0, curLetter)
            if curPointer - 1 > 0:
                if not reg.match(inputString[curPointer-1]):
                    maxMatchedString.insert(0, convertListOfCharToString(possibleWord))
                    possibleWord = []
            else:
                break
        else:
            possibleWord.insert(0, curLetter)
            if dictRef.__contains__(convertListOfCharToString(possibleWord)):
                #look ahead to end of string to see if a slightly longer word can be matched
                #if so, it's the more likely word.
                another_possibility = [y for y in possibleWord]
                dist_to_end_of_string = curPointer
                curIndex = curPointer
                pointerTracker = curPointer
                for z in range(1, dist_to_end_of_string + 1):
                    another_possibility.insert(0, inputString[curIndex - z])
                    if dictRef.__contains__(convertListOfCharToString(another_possibility)):
                        possibleWord = [x for x in another_possibility]
                        pointerTracker = curPointer - z

                curPointer = pointerTracker
                maxMatchedString.insert(0, convertListOfCharToString(possibleWord))
                possibleWord = []

        curPointer -= 1

    if len(maxMatchedString) == 0:
        maxMatchedString = [inputString.rstrip()]
    return maxMatchedString

def convertListOfCharToString(list):
    st = ''
    for char in list:
        st += char
    return st


def maxMatchImprovedAllTagsAndOutputToFile(listOFHashTags, dictRef, outFileName):

    fo = open(outFileName, 'w')

    answersInListForm = []

    for hashTag in listOFHashTags:
        maxMatchList = maxMatchImproved(hashTag, dictRef)
        answersInListForm.append(maxMatchList)
        outLine = ""
        for word in maxMatchList:
            outLine += word + " "

        fo.write(outLine + "\n")

    fo.close()

    return answersInListForm

def maxMatchAllTagsAndOutputToFile(listOFHashTags, dictRef, outFileName):

    fo = open(outFileName, 'w')

    answersInListForm = []

    for hashTag in listOFHashTags:
        maxMatchList = maxMatch(hashTag, dictRef)
        answersInListForm.append(maxMatchList)
        outLine = ""
        for word in maxMatchList:
            outLine += word + " "

        fo.write(outLine + "\n")

    fo.close()

    return answersInListForm





















