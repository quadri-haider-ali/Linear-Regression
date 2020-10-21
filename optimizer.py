import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from lossFunction import loss
import time
fig = plt.figure()
def gradientDescent(x,y,m,c,alpha,epochs,plot):
    for epoch in range(epochs):
        loss_ = loss(x,y,m,c)
        print("loss = {}".format(loss_))
        print("m = ",m)
        print("c = ",c)
        h=m*x+c
        error = h-y
        m-=(alpha/len(x)) * np.dot(error,x)
        c-=(alpha/len(x)) * np.dot(error,np.ones(np.shape(x)))
        i=0
        if plot:
            # style.use('fivethirtyeight')
            xtemp = np.linspace(-10,10,100)
            ytemp = m*xtemp+c
            print("plt prints ", m,c)
            plt.plot(xtemp,ytemp,'-r',label = "y={}x+{}".format(m,c))
            plt.plot(xtemp,2*xtemp,'-b',linestyle='--')
            plt.grid()
            plt.show(block=False)
            plt.pause(0.05)
            plt.clf()
        print("========================================")
    return m,c