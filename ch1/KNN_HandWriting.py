#-*- coding=utf-8 -*-
import os

import numpy as np

import kNN


#读取一个32*32的个数字到1024的向量中
def img2vector(fileName):
    returnVect = np.zeros((1, 1024))
    f = open(fileName)

    for i in range(32):
        line = f.readline()
        for j in range(32):
            returnVect[0, 32*i+j] = int(line[j])

    f.close()
    return returnVect

def getLabelByFileName(fileName):
    return int(fileName.split(".")[0].split("_")[0])



def handWritingClassTest(trainingFilePath, testFilePath):
    errorCount = 0.0
    hwLabel = []
    trainingFileList = os.listdir(trainingFilePath)
    trainingNum = len(trainingFileList)
    trainingMat = np.zeros((trainingNum, 1024))
    for i in range(trainingNum):
        trainingMat[i, :] = img2vector('%s/%s'% (trainingFilePath, trainingFileList[i]))
        hwLabel.append(getLabelByFileName(trainingFileList[i]))

    testFileList = os.listdir(testFilePath)
    testNum = len(testFileList)
    for i in range(testNum):
        testVector = img2vector('%s/%s'% (testFilePath, testFileList[i]))
        realResult = getLabelByFileName(testFileList[i])
        estimateResult = kNN.classify0(testVector, trainingMat, hwLabel, 3)
        if(estimateResult != realResult):
            errorCount += 1.0
            print("realResult=%d, estimateResult=%d." % (realResult, estimateResult))

    print("error Rate =%f." % (errorCount / float(testNum)))


def main():
    np.set_printoptions(threshold=np.nan)
    handWritingClassTest("D:/workspace/python/ml/machinelearninginaction/Ch02/trainingDigits",
                         "D:/workspace/python/ml/machinelearninginaction/Ch02/testDigits")

if __name__ == '__main__':
    main()




