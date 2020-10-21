import numpy as np

def readtxt(file):
    file = open(file,'r')

    x=[]
    y=[]

    for line in file:
        splitLine = line.split(' ')
        x.append(int(splitLine[0]))
        y.append(int(splitLine[1].strip()))

    file.close()
    return np.array(x),np.array(y)