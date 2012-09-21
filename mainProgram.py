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

#aHashTag = sampleHashTags[3]
#print aHashTag
#correctTag = sampleHashTagsWithAnswers.get('#' + aHashTag)
#print correctTag
#matchTag = MaxMatch.maxMatch(aHashTag, lexicon)
#matchTag = MaxMatch.maxMatchImproved(aHashTag, lexicon)

#MaxMatch.maxMatchAllTagsAndOutputToFile(sampleHashTags, lexicon, 'maccoun-out-assgn1.txt')

testFile = open('testSet.txt', 'r')
testSet = []
for line in testFile:
    hashTagWithoutPound = line.replace('#', '')
    hashTagWithoutPound = hashTagWithoutPound.lower()
    testSet.append(hashTagWithoutPound)

testMaxMatch = MaxMatch.maxMatchAllTagsAndOutputToFile(testSet, lexicon, 'maccoun-out-assgn1.txt')
print "testMaxMatch: " , testMaxMatch

answers = [['london','2012'],
            ['switch','to','chrome'],
            ['iphone5'],
            ['team', 'gb'],
            ['47','percent'],
            ['nbc','fail'],
            ['art','of','letter','writing','is','almost','lost'],
            ['conspiracy','theories','for','breakfast'],
            ['doctors', 'without','borders'],
            ['iran'], ['election'],
            ['tomorrows'],['news'],['today'],
            ['its','the','thought','that','counts'],
            ['yankees','get','another','call'],
            ['someone','dropped','the','ball'],
            ['missed','opportunities'],
            ['earthquake','in','haiti'],
            ['loveland','ski','area'],
            ['bmw','championship'],
            ['deforestation'],
            ['pumpkin','chocolate','chip','cookie','recipe']]

#print MinNumberEdits.computeMinNumberEdits(source, target)



