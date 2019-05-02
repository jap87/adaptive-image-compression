import pandas as pd
import numpy as np 
from matplotlib import pyplot as plt 
from numpy import genfromtxt
import random

def plotMaskChange():
    dataPointsPerSample = 30
    df = genfromtxt('maskRegression.csv', delimiter=',')
    print()
    y = df[:,1]/df[:,2] 
    numSamples = int(len(df)/dataPointsPerSample)
    print(numSamples)
    for i in range(numSamples):
        color = np.array([random.random(), random.random(), random.random(), .5])
        offset = dataPointsPerSample*i
        x = df[offset:offset+dataPointsPerSample,0]
        yPlot = y[offset:offset+dataPointsPerSample]
        plt.plot(x,yPlot,c=color)
        plt.scatter(x,yPlot,c=color, marker = '.')
    plt.title('Mask Size vs Compression Ratio | Quality = 30')
    plt.xlabel('Mask Size (% Total Area)')
    plt.ylabel('Compression Ratio (Relative to PNG)')
    plt.show()

plotMaskChange()