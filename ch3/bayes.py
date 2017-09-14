#coding:utf-8
import random
import numpy as np

def loadDataSet():
    """
    创建数据集
    :return: 单词列表postingList, 所属类别classVec
    """
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'], #[0,0,1,1,1......]
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 1 is abusive, 0 not
    return postingList, classVec


def createVocabList(dataSet):
    vocabSet = set([])
    for part in dataSet:
        vocabSet |= set(part)
    return list(vocabSet)


def setOfWords2Vec(vocabList, inputSet):
    retVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            retVec[vocabList.index(word)] = 1
        else:
            print("The word %s is not in vacobulary."% (word))
    return retVec


def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numTotalWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory) / float(numTrainDocs)

    p0Num = np.ones(numTotalWords)
    p1Num = np.ones(numTotalWords)
    p0Denom = 2.0
    p1Denom = 2.0

    for i in range(numTrainDocs):
        if trainCategory[i] == 0:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])

        else:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])

    p0Num = np.log(p0Num/p0Denom)  #此处进行优化，因为考虑到分母可能为0，所以改为求ln
    p1Num = np.log(p1Num/p1Denom)
    return pAbusive, p0Num, p1Num  #返回先验概率，以及两个条件概率的向量


def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(p1Vec * vec2Classify) + np.log(pClass1)
    p0 = sum(p0Vec * vec2Classify) + np.log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0


def testingNB():
    dataSetList, labelVec = loadDataSet()
    vecabList = createVocabList(dataSetList)
    trainMatix = []
    for dataList in dataSetList:
        trainMatix.append(setOfWords2Vec(vecabList, dataList))

    pAb, p0Vec, p1Vec = trainNB0(trainMatix, labelVec)
    testEntry = setOfWords2Vec(vecabList ,["love", "my", "dalmation"])
    retValue = classifyNB(testEntry, p0Vec, p1Vec, pAb)
    print(retValue)

    testEntry = setOfWords2Vec(vecabList, ["stupid", "grabage"])
    retValue = classifyNB(testEntry, p0Vec, p1Vec, pAb)
    print(retValue)


def textParse(bigStr):
    import re
    listOfTokens = re.split(r'\W*', bigStr)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]

def spamTest():
    docList = []; classList = []; fullText = []
    for i in range(1,26):
        wordList = textParse(open("D:\\workspace\\python\\ml\\MachineLearning\\input\\4.NaiveBayes\\email\\ham\\%d.txt" % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)

        wordList = textParse(open("D:\\workspace\\python\\ml\\MachineLearning\\input\\4.NaiveBayes\\email\\spam\\%d.txt" % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)

    vocabList = createVocabList(docList)
    trainingSet = range(50)
    testSet  = []
    for i in range(10):
        randomIdx = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randomIdx])
        del(trainingSet[randomIdx])
    trainMat = []; trainCategory = []
    for docIndex in trainingSet:
        trainMat.append(setOfWords2Vec(vocabList, docList[docIndex]))
        trainCategory.append(classList[docIndex])
    pSpam, p0V, p1V = trainNB0(trainMat, trainCategory)

    errorCount = 0
    for docIndex in testSet:
        docVec = setOfWords2Vec(vocabList, docList[docIndex])
        classifyRet = classifyNB(docVec, p0V, p1V, pSpam)
        if classifyRet != classList[docIndex]:
            print("The estaimate is Wrong.. docIndex=%d." % docIndex)
            errorCount += 1
    print("error rate =%f."% (float(errorCount)/float(len(testSet))))


if __name__ == '__main__':
    #testingNB()
    spamTest()