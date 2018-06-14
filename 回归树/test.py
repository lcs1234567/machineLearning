from numpy import *

def loadDataSet(fileName):
    """loadDataSet(解析每一行，并转化为float类型)
        Desc：该函数读取一个以 tab 键为分隔符的文件，然后将每行的内容保存成一组浮点数
    Args:
        fileName 文件名
    Returns:
        dataMat 每一行的数据集array类型
    Raises:
    """
    # 假定最后一列是结果值
    # assume last column is target value
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        # 将所有的元素转化为float类型
        # map all elements to float()
        # map() 函数具体的含义，可见 https://my.oschina.net/zyzzy/blog/115096
        fltLine = list(map(float, curLine))
        dataMat.append(fltLine)
    return dataMat


myDat = loadDataSet('../input/9.RegTrees/data1.txt')

print(myDat)
myMat = mat(myDat)

a = myMat[:,-1]

print(mean(a))