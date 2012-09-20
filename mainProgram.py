__author__ = 'theraccoun'

import MaxMatch
import MinNumberEdits
from LexiconImprovement import LexiconImprover


hashTagFile = open('hashtags-dev.txt', 'r')
bigWordsFile = open('bigwordlist.txt', 'r')


NUMBER_OF_WORDS = 75000
lexicon = []

for i in range(NUMBER_OF_WORDS):
    line = bigWordsFile.readline()
    wordOnly = line.split()[0]
    wordOnly.replace(" " , "")
    if len(wordOnly) >= 1:
        lexicon.append(wordOnly)

#improve the lexicon by removing infrequent words that are relatively few letters in length
lexImprover = LexiconImprover(lexicon)
lexicon = lexImprover.improveLexicon()

allHashTags = hashTagFile.readlines()



sampleHashTagsWithAnswers = {'#30secondstomars' : ['30', 'seconds', 'to', 'mars'],
                             '#americanidol' : ['american', 'idol'],
                             '#hurricaneike' : ['hurricane', 'ike'],
                             '#celebraterandommilestones' : ['celebrate' , 'random' , 'milestones'],
                             '#entrepreneurship' : ['entrepeneurship'],
                             '#firstdayofkindergarten' : ['first', 'day' , 'of' , 'kindergarten']}


sampleHashTags = []

for key in sampleHashTagsWithAnswers:
    hashTagWithoutPound = key.replace('#', '')
    sampleHashTags.append(hashTagWithoutPound)

print sampleHashTags

aHashTag = sampleHashTags[3]
print aHashTag
correctTag = sampleHashTagsWithAnswers.get('#' + aHashTag)
print correctTag
#matchTag = MaxMatch.maxMatch(aHashTag, lexicon)
matchTag = MaxMatch.maxMatchImproved(aHashTag, lexicon)

print 'matchTag: ' , matchTag
#target = ["puppy", "is", "walking"]
#source = ["moose", "is", "jumping"]

source = matchTag
target = correctTag
print "target: " , target

print MinNumberEdits.computeMinNumberEdits(source, target)



