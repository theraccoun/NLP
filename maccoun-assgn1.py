__author__ = 'theraccoun'

import MaxMatch
import MinNumberEdits
from LexiconImprovement import LexiconImprover
import re


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


lexImprover = LexiconImprover(lexicon)
lexicon = lexImprover.improveLexicon()
#improve the lexicon by removing infrequent words that are relatively few letters in length

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
    correctHashTag = hashTagWithoutPound.replace('\n', '')
    correctHashTag = correctHashTag.lower()
    testSet.append(correctHashTag)

#testMaxMatch = MaxMatch.maxMatchAllTagsAndOutputToFile(testSet, lexicon, 'maccoun-out-assgn1-part1.txt')


testMaxMatchImprove = MaxMatch.maxMatchImprovedAllTagsAndOutputToFile(testSet, lexicon, 'maccoun-out-assgn1-part3.txt')

answers = [['london','2012'],
            ['switch','to','chrome'],
            ['iphone', '5'],
            ['team', 'gb'],
            ['47','percent'],
            ['nbc','fail'],
            ['art','of','letter','writing','is','almost','lost'],
            ['conspiracy','theories','for','breakfast'],
            ['doctors', 'without','borders'],
            ['iran','election'],
            ['tomorrows','news','today'],
            ['its','the','thought','that','counts'],
            ['yankees','get','another','call'],
            ['someone','dropped','the','ball'],
            ['missed','opportunities'],
            ['earthquake','in','haiti'],
            ['loveland','ski','area'],
            ['bmw','championship'],
            ['deforestation'],
            ['pumpkin','chocolate','chip','cookie','recipe']]


MinNumberEdits.computeAllWER(answers, testMaxMatchImprove)



