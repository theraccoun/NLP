__author__ = 'theraccoun'

def maxMatch(inputString, dictRef):
    possibleWord = ''
    maxMatchedString = []

    for letter in inputString:
        possibleWord += letter
        print "letter: " + letter
        print "pw: " + possibleWord

        if dictRef.__contains__(possibleWord):
            print "matched: " , possibleWord
            maxMatchedString.append(possibleWord)
            possibleWord = ''

    print maxMatchedString
    return maxMatchedString

def maxMatchImproved(inputString, dictRef):
    possibleWord = ''
    maxMatchedString = []

    at_end_of_input_string = False
    i = 0
    while not at_end_of_input_string:
        if i > len(inputString) - 1:
            break
        letter = inputString[i]
        possibleWord += letter
        print "letter: " + letter
        print "pw: " + possibleWord

        if dictRef.__contains__(possibleWord):
            print "matched: " , possibleWord
            #look ahead five letters to see if a slightly longer word can be matched
            #if so, it's the more likely word. This is likely only true if the word is
            #longer than 6 letters
            if len(possibleWord) >= 3 or len(possibleWord) == 1:
                another_possibility = possibleWord
                curIndex = i
                dist_to_end_of_string = len(inputString) - i
                for z in range(1, dist_to_end_of_string):
                    print curIndex,z
                    lookAhead = curIndex + z
                    another_possibility += inputString[lookAhead]
                    print "another_Pos: " , another_possibility
                    if dictRef.__contains__(another_possibility):
                        possibleWord = another_possibility
                        i = curIndex + z
                        print "matched" , z , "ahead: " , possibleWord


            maxMatchedString.append(possibleWord)
            possibleWord = ''

        i += 1

    print maxMatchedString
    return maxMatchedString


















