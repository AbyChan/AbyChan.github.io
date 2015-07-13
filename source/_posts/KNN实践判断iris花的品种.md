title: KNN实践判断iris花的品种
date: 2015-01-28 12:17:27
tags:
- 机器学习
- k邻近
- 算法
- knn
---

k邻近（KNN）算法应该是机器学习算法中最简单的一个吧。
kNN(k Nearest Neighbors)算法又叫k最临近方法， 总体来说kNN算法是相对比较容易理解的算法之一，假设每一个类包含多个样本数据，而且每个数据都有一个唯一的类标记表示这些样本是属于哪一个分类， kNN就是计算每个样本数据到待分类数据的距离，取和待分类数据最近的k各样本数据，那么这个k个样本数据中哪个类别的样本数据占多数，则待分类数据就属于该类别。
不过KNN的不足也很明显，计算量大，每一个判断输入都要扫一遍数据集，而且没有训练过程。
在UCI
http://archive.ics.uci.edu/ml/datasets/Iris
找到了一些数据集，数据算是非常简单了

```python

from numpy import *
import os
from collections import Counter

def dataPre(filePath):
    fr = open(filePath)
    fileNumber = len(fr.readlines())
    fr = open(filePath)
    simpleLine = fr.readline()
    simpleLine = simpleLine.strip()
    colNumber = len(simpleLine.split(',')) - 1
    retMat = zeros((fileNumber, colNumber))
    classLabel = []
    index = 0
    fr = open(filePath)
    for line in fr.readlines():
        line = line.strip()
        cols = line.split(',')
        retMat[index,:] = cols[0 : colNumber]
        classLabel.append(cols[colNumber])
        index += 1
    return Norm(retMat), classLabel

def Norm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals = minVals
    normDataSet = zeros(shape(dataSet))
    m = len(dataSet)
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))
    return normDataSet

def classify(dataSet, dataSetLabel, input, k):
    iCols = input
    print len(dataSet[0])
    if len(dataSet[0]) != len(iCols):
        print 'Input Error'
        return
    diffMat = tile(iCols, (len(dataSet),1)) - dataSet
    sqDistancesMat = (diffMat**2).sum(axis=1)
    distances = sqDistancesMat**0.5
    sortedDistances = distances.argsort()
    classCount = []
    for i in range(k):
        predictLabel = dataSetLabel[sortedDistances[i]]
        classCount.append(predictLabel)
    frequent = Counter(classCount)
    return frequent.most_common(1)[0][0]
```
