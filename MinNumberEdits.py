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

    print "second assign " , distance

    print distance

    for i in range(1, targLen+1):
        for j in range(1, sourceLen+1):

            if target[i-1] == source[j-1]:
                sub_cost = 0
                print "same: " + target[i-1]
            else:
                sub_cost = 1

            print "ins: " , distance[i-1][j] + INS_COST
            print "sub: " , distance[i-1][j-1] + sub_cost
            print "del: " , distance[i][j-1] + DEL_COST

            distance[i][j] = min(distance[i-1][j] + INS_COST,
                                distance[i-1][j-1] + sub_cost,
                                distance[i][j-1] + DEL_COST)

    return distance[targLen][sourceLen]



