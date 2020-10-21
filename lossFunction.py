import numpy as np

def loss(x,y,theta1,theta0):
    h=theta1*x+theta0
    return np.sum((y-h)**2)/(2*len(x))