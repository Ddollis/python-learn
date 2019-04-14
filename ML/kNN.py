from numpy import *


def createDataSet():
    group = array([[1.0, 1.1],
                   [1.0, 1.0],
                   [0, 0],
                   [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distance = sqDistances ** 0.5
    sortedDistIndices = distance.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndices[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.iteritems(),
                              key=operator.itemgetter(1),
                              reverse=True)
    return sortedClassCount[0][0]


group, labels = createDataSet()
classify0([0, 0], group, labels, 3)


def file2matrix(filename):
    fr = open(filename)
    arrayLines = fr.readlines()
    numberOfLines = len(arrayLines)
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayLines:
        listForLine = line.split('\t')
        returnMat[index, :] = listForLine[:-1]
        classLabelVector.append(int(listForLine[-1]))
        index += 1
    return returnMat, classLabelVector


# datingDateMat, datingLabels = file2matrix('C:\Users\Administrator\Desktop\python-learn\ML\datingTestSet2.txt')
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(datingDateMat[:, 1], datingDateMat[:, 2], 15.0 * array(datingLabels), 15.0 * array(datingLabels))
# plt.show()

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))
    return normDataSet, ranges, minVals


# normMat, ranges, minVals = autoNorm(datingDateMat)

def datingClassTest():
    hoRatio = 0.10
    datingDateMat, datingLabels = file2matrix('C:\Users\Administrator\Desktop\python-learn\ML\datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDateMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:, ], datingLabels[numTestVecs:], 4)
        print 'the classifier came back with: %d, the real answer: %d' % (classifierResult, datingLabels[i])
        if classifierResult != datingLabels[i]:
            errorCount += 1.0
    print "the total error rate is: %f" % (errorCount / float(numTestVecs))


# datingClassTest()
def classifyPerson():
    resultList = ['not at all', 'in small doses', 'int large doses']
    percentTats = float(raw_input('percentage of time spend playing video games?'))
    ffMails = float(raw_input('frequent flier miles earned per year?'))
    iceCream = float(raw_input('liters of ice-cream consumed per year?'))
    datingDateMat, datingLabels = file2matrix('C:\Users\Administrator\Desktop\python-learn\ML\datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDateMat)
    inArr = array([percentTats, ffMails, iceCream])
    classifierResult = classify0((inArr - minVals) / ranges, normMat, datingLabels, 3)
    print 'You will probably like this person:', resultList[classifierResult - 1]


classifyPerson()
