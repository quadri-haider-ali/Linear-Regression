import numpy as np
from readData import readtxt
from lossFunction import loss
from optimizer import gradientDescent

if __name__=="__main__":
    x,y=readtxt('data.txt')
    m,c=gradientDescent(x,y,0,0,0.01,35,True)
    print("M = ",m)
    print("C = ",c)