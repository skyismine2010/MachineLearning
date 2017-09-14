#-*-coding: utf-8-*-
from numpy import *
import matplotlib
import matplotlib.pyplot as plt
import operator

def CreateDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    print(group.shape)
    labels = ['A', 'A', 'B', 'B']
    return group, labels


#inX：用于分类的输入向量
#dataSet:训练样本集
#labels： 训练标签
#k:临近k值
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]   #这里是ndarray矩阵的行数
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet  #这里是一个矩阵的计算,先构造一个和dataSet的行数一样大小的矩阵
    #print(diffMat)
    sqDiffMat = diffMat ** 2   #计算平方
    sqDistances = sqDiffMat.sum(axis=1) #计算求和， 计算inX和所有节点直接的距离,这是一个数组
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel]  = classCount.get(voteIlabel, 0) + 1  #如果voteILabel在Dict中，则取出其值+1，如果不在Dict中，则返回默认值0 +1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]


def printFig(mat, vec):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(mat[:, 1], mat[:, 2], 15.0*array(vec), 15*array(vec))
    plt.show()


def file2matrix(filename):
    fr = open(filename)
    arrayOfLines = fr.readlines()

    numberOfLines = len(arrayOfLines)
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayOfLines:
        line = line.strip()
        listFromLine = line.split("\t")
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector


def datingClassTest():
    hoRatio = 0.10
    datingDataSet, datingLabel = file2matrix("D:\workspace\python\ml\machinelearninginaction\Ch02\datingTestSet2.txt")
    normMat, rangeVector, minVector = autoNorm(datingDataSet) #进行归一化的处理，返回归一化矩阵，范围向量，最小值向量
    m = normMat.shape[0]
    numTest = int(m * hoRatio)  #待测试的数据集
    errorCount = 0.0
    for i in range(numTest):
        classifyResult = classify0(normMat[i, :], normMat[numTest:m, :], datingLabel[numTest:m], 3)
        print("classify return %d, The true answer is %d." % (classifyResult, datingLabel[i]))
        if(classifyResult != datingLabel[i]):
            errorCount += 1.0
    print("errorCount = %d, The total error rate is %f." %( errorCount, errorCount / float(numTest)) )


def autoNorm(dataSet):
    minVector = dataSet.min(0)
    print("minVector = %s" % (minVector))
    maxVector = dataSet.max(0)
    print("maxVector = %s" % (maxVector))
    rangeVector = maxVector - minVector
    print("rangeVector= %s" % (rangeVector))
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVector, (m, 1))
    normDataSet = normDataSet / tile(rangeVector, (m, 1))
    return normDataSet, rangeVector, minVector

'''
def main():
    datingClassTest()

if __name__ == "__main__":
    main()
'''
