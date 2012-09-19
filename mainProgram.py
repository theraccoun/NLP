__author__ = 'theraccoun'

import MaxMatch
import MinNumberEdits

hashTagFile = open('hashtags-dev.txt', 'r')
bigWordsFile = open('bigwordlist.txt', 'r')


NUMBER_OF_WORDS = 75000
lexicon = []

for i in range(NUMBER_OF_WORDS):
    line = bigWordsFile.readline()
    wordOnly = line.split()[0]
    if len(wordOnly) >= 1:
        lexicon.append(wordOnly)


allHashTags = hashTagFile.readlines()

sampleHashTags = {'#30secondstomars' : ['30', 'seconds', 'to', 'mars'],
                  '#americanidol' : ['american', 'idol'],
                  '#hurricaneike' : ['hurricane', 'ike'],
                  'celebraterandommilestones' : ['celebrate' , 'random' , 'milestones'],
                  '#entrepreneurship' : ['entrepeneurship'],
                  '#firstdayofkindergarden' : ['first', 'day' , 'of' , 'kindergarden']}

for hashTag in sampleHashTags:
    hashTag.replace("#", '')

aHashTag = sampleHashTags.keys()[1]
correctTag = sampleHashTags.get(aHashTag)
matchTag = MaxMatch.maxMatch(aHashTag, lexicon)

print 'matchTag: ' , matchTag
#target = ["puppy", "is", "walking"]
#source = ["moose", "is", "jumping"]

source = matchTag
target = correctTag
print "target: " , target

print MinNumberEdits.computeMinNumberEdits(source, target)