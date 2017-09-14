#coding:utf-8
import math
import numpy as np

#加载函数
def loadDataSet():
    dataMat = []; labelMat=[]
    f = open("D:\\workspace\\python\\ml\\MachineLearning\\input\\5.Logistic\TestSet.txt")
    for line in f.readlines():
        lineList = line.strip().split()
        dataMat.append([1.0, float(lineList[0]), float(lineList[1])])
        labelMat.append([lineList[2]])
    return dataMat, labelMat

def sig_mod(x_vec):
    return  1 / (1 + math.e ** (-1 * x_vec))


def gradAscent(dataMatIn, classLabels):
    dataMatrix = np.mat(dataMatIn)
    labelMat = np.mat(classLabels).transpose()
    m,n = dataMatrix.shape
    alpha = 0.01
    maxCycles = 500
    weights = np.ones((n, 1))
    for k in range(maxCycles):
        h = sig_mod(dataMatrix * weights)
        error = (lab)





if __name__ == '__main__':
    dataMat, labelMat = loadDataSet()
    print(dataMat)
