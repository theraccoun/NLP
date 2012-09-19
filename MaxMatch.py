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


















