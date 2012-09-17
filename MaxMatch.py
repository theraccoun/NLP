__author__ = 'theraccoun'

hashTagFile = open('hashtags-dev.txt', 'r')
bigWordsFile = open('bigwordlist.txt', 'r')


NUMBER_OF_WORDS = 75000
corpus = []

for i in range(NUMBER_OF_WORDS):
    line = bigWordsFile.readline()
    wordOnly = line.split()[0]
    if len(wordOnly) > 1:
        corpus.append(wordOnly)


allHashTags = hashTagFile.readlines()

sampleHashTags = {'#30secondstomars' : '30 seconds to mars',
                  '#americanidol' : 'american idol',
                  '#hurricaneike' : 'hurricane ike',
                  'celebraterandommilestones' : 'celebrate random milestones',
                  '#entrepreneurship' : 'entrepeneurship',
                  '#firstdayofkindergarden' : 'first day of kindergarden'}

for hashTag in sampleHashTags:
    hashTag.replace("#", '')

def maxMatch(inputString, dictRef):
    possibleWord = ''
    maxMatchedString = []

    for letter in inputString:
        possibleWord += letter
        print "letter: " + letter
        print "pw: " + possibleWord
        if dictRef.__contains__(possibleWord):
            maxMatchedString.append(possibleWord)
            possibleWord = ''

    print maxMatchedString
    return

maxMatch('peachpie', corpus)


















