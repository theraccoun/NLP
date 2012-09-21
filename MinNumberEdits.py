__author__ = 'theraccoun'

INS_COST = 1
DEL_COST = 1
sub_cost = 1

def computeMinNumberEdits(target, source):
    targLen = len(target)
    sourceLen = len(source)
    print targLen, sourceLen


# Initizialize a 2d array
    distance = [[0 for y in range(sourceLen + 1)] for x in range(targLen+1)]
    print "dist = " + str(len(distance[0]))
    distance[0][0] = 0

    for i in range(1, targLen+1):
        distance[i][0] = distance[i-1][0] + INS_COST
    print "first assign: " , distance
    for j in range(1, sourceLen + 1):
        distance[0][j] = distance[0][j-1] + DEL_COST


    for i in range(1, targLen+1):
        for j in range(1, sourceLen+1):

            if target[i-1] == source[j-1]:
                sub_cost = 0
                print "same: " + target[i-1]
            else:
                sub_cost = 1

            distance[i][j] = min(distance[i-1][j] + INS_COST,
                                distance[i-1][j-1] + sub_cost,
                                distance[i][j-1] + DEL_COST)

    return distance[targLen][sourceLen]

def computeWER(target, source):
    return float(computeMinNumberEdits(target, source))/float(len(target))

def computeAllWER(targetList, sourceList):
    statFile = open('werStats.txt', 'w')
    allWER = []
    print "source: " , sourceList
    print "target: " , targetList
    if len(targetList) != len(sourceList):
        print len(targetList), len(sourceList)
        return
    for i in range(len(targetList)):
        my_output = sourceList[i]
        target = targetList[i]
        wer = computeWER(target, my_output)
        allWER.append(wer)
        print "********************\n Answer: " , target , "\n myOutput: " , my_output , "\n wer: " , str(wer), "\n ***********************"
        targetString = ""
        for t in target:
            targetString += t + " "
        print "targSTring: " + targetString
        outputString = ""
        for o in my_output:
            outputString += o + " "
        line = "Answer: " + targetString + "\nOutput: " + outputString + "\n WER: " + str(wer) + "\n----------------------------------\n"
        statFile.write(line)

    sumAllWER = 0
    for w in allWER:
        sumAllWER += w
    print sumAllWER
    print len(allWER)
    averageWER = float(sumAllWER)/float(len(allWER))
    print "AVERAGE WER: " , averageWER
    statFile.write("\n**********************\n Average WER = " + str(averageWER) + "\n**************************\n")



