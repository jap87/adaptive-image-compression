import pandas as pd
import numpy as np 
from matplotlib import pyplot as plt 
from numpy import genfromtxt
import random

def plotMaskChange():
    dataPointsPerSample = 30
    df = genfromtxt('maskRegression.csv', delimiter=',')
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

def plotMaskChange():
    numIm = 11
    dataPointsPerSample = 31
    df = genfromtxt('backup.csv', delimiter=',')
    x = df[:,3]
    y = df[:,1]/df[:,2]/2
    numSamples = int(len(df)/dataPointsPerSample)
    for i in range(numSamples):
        color = np.array([random.random(), random.random(), random.random(), .5])
    
        offset = i
        xPlot = x[i::numIm]
        yPlot = y[i::numIm]
        print(xPlot.shape)

        plt.plot(xPlot,yPlot,c=color)
        plt.scatter(xPlot,yPlot,c=color, marker = '.')
    plt.title('JPEG Quality vs Compression Ratio | Mask Size = .4 Total')
    plt.xlabel('JPEG Quality')
    plt.ylabel('Compression Ratio (Relative to PNG)')
    plt.show()

def plotThing():
    dataPointsPerSample = 30
    df0 = genfromtxt('jpeg30.csv', delimiter=',')
    df1 = genfromtxt('blur.csv', delimiter=',')

    y0 = df0[:,1]/df0[:,2]
    y1 = df1[:,1]/df1[:,2]
    y3 = y0*.9+.1
    x = df0[:,0]

    offset = 0
   
    plt.scatter(x,y0, marker = '.')
    plt.scatter(x,y1, marker = '.')
    plt.scatter(x,y3, marker = '.')
    plt.title('Mask Size vs Compression Ratio per Entropy Technique')
    plt.xlabel('Mask Size (% Total Area)')
    plt.ylabel('Compression Ratio (Relative to PNG)')
    plt.legend(['jp2 - quality:30','disk blur: 5x5 kernel', 'jpeg - quality:30'])
    plt.show()



plotThing()