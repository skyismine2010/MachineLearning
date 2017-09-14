#-*-coding: utf-8-*-
import operator
from math import log
import matplotlib.pyplot as plt

#计算熵的期望函数
def calcShannonEnt(dataSet):
    dataSetLen = len(dataSet)

    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0
    for key in labelCounts:
        prob = float( labelCounts[key] )/  dataSetLen
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet


def createDataSet():
    dataSet = [ [1, 1, "yes"],
                [1, 1, "yes"],
                [1, 0, "no"],
                [0, 1, "no"],
                [0, 1, "no"],
                ]
    labels = ["no surfacing", "flippers"]
    return dataSet, labels


def chooseBestFeatureToSplit(dataSet):
    featuresNum = len(dataSet[0]) - 1
    bestEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(featuresNum):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0

        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / len(dataSet)
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = bestEntropy - newEntropy
        if(infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def createTree(dataSet, label):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0])  == len(classList): #如果数据集中的所有都是一种分类，即返回此分类，此时返回的就是决策树的叶子节点
        return classList[0]

    if len(dataSet[0]) == 1:  #特征值只剩下1个，返回当前数据集中数量最多的那种分类，此时返回的就是决策树的叶子节点
        return majorityCnt(classList)

    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = label[bestFeat]
    myTree = {bestFeatLabel : {}}
    del(label[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueFeatValues = set(featValues)
    for value in uniqueFeatValues:
        subLabel = label[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabel)
    return myTree


def main():
    dataSet, labels = createDataSet()
    print(dataSet)
    '''shannonEnt = calcShannonEnt(dataSet)
    print(shannonEnt)
    ret = splitDataSet(dataSet, 1, 0)
    print(ret)
    '''
    myTree = createTree(dataSet, labels)
    print(myTree)



if __name__ == '__main__':
    main()
