import math
import copy
import operator
import treePlotter

def calcShanonEnt(dataSet):
    numEntries = len(dataSet)
    labelCount = {}

    for sample in dataSet:
        if sample[-1] not in labelCount.keys():
            labelCount[sample[-1]] = 0
        labelCount[sample[-1]] += 1

    shanonEnt = 0.0
    for key in labelCount.keys():
        prob = float(labelCount[key] / numEntries)
        shanonEnt -= prob * math.log(prob, 2)
    return shanonEnt


def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no'],
               ]

    label = ['no surfacing', 'flippers']
    return dataSet, label


def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for sample in dataSet:
        if sample[axis] == value:
            reducedFeatVec = sample[:axis]
            reducedFeatVec.extend(sample[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet


def chooseBestFeatureToSplit(dataSet):
    newFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShanonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1

    for i in range(newFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = float(len(subDataSet) / len(dataSet))
            newEntropy += prob * calcShanonEnt(subDataSet)

        infoGain = baseEntropy - newEntropy
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


def createTree(dataSet, labels):
    #先取出当前所有的类别
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]

    #如果只有一列了，那就说明已经没必要再继续特性分割
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)

    #选择一个最好的待分割的特性
    bestFeat = chooseBestFeatureToSplit(dataSet)
    print("bestFeat=", bestFeat)

    bestFeatLabel = labels[bestFeat]

    myTree = {bestFeatLabel: {}}
    del(labels[bestFeat])

    #去重复特征，得到特征的取值范围（枚举值）
    uniqueFeatValues = set([example[bestFeat] for example in dataSet])


    for value in uniqueFeatValues:
        sublabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), sublabels)

    return myTree


def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1

    sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return classCount[0][0]


def classifty(inputTree, featLabels, testVec):
    classLabel = ""
    firstStr = list(inputTree.keys())[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():
        if key == testVec[featIndex]:
            if type(secondDict[key]).__name__ == 'dict':
                return classifty(secondDict[key], featLabels, testVec)
            else:
                return secondDict[key]


def main():
    dataSet, labels = createDataSet()
    myTree = createTree(dataSet, copy.deepcopy(labels))
    print(myTree)
    print(labels)
    treePlotter.createPlot(myTree)
    storeTree(myTree, "tree.txt")
    print(classifty(myTree, labels, [1, 0]))
    print(classifty(myTree, labels, [1, 1]))



def storeTree(inputTree, filename):
    import pickle
    # fw = open(filename, 'w')
    # pickle.dump(inputTree, fw)
    # fw.close()
    with open(filename, 'wb+') as fw:
        pickle.dump(inputTree, fw)




def grapTree(filename):
    import pickle
    with open(filename, 'r') as fr:
        return pickle.load(fr)


if __name__ == '__main__':
    main()