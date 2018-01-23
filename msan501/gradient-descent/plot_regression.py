from pylab import show, text, imshow, plot
import matplotlib.pyplot as plt
import random
import time

from minimize import *

# Average hourly wage
HOURLY_WAGE = [2.98, 3.09, 3.23, 3.33, 3.46, 3.6, 3.73, 2.91, 4.25, 4.47, 5.04, 5.47, 5.76]
# Number of homicides per 100,000 people
MURDERS = [8.6, 8.9, 8.52, 8.89, 13.07, 14.57, 21.36, 28.03, 31.49, 37.39, 46.26, 47.24, 52.33]

B0= [random.randrange(-60,-14),random.randrange(5,26)]
LEARNING_RATE = 3000
h = 0.0000001
PRECISION = 0.0000001

def Cost(B,X=HOURLY_WAGE,Y=MURDERS):
	cost = 0.0
	for i in xrange(0,len(X)):
		cost += (B[1]*X[i] + B[0] - Y[i])**2
	return cost


def heatmap(f, trace=None): # trace is a list of [b1, b2] pairs
    b1 = np.arange(-60,-14,.1)
    b2 = np.arange(5,26,.1)
    C = np.empty([len(b1), len(b2)])
    for i in range(len(b1)):
        for j in range(len(b2)):
            C[i][j] = f([b1[i],b2[j]])


    for p in trace:
        plt.plot(p[0], p[1], "ko", markersize=1)

    imshow(C,  # this is C[row][col]
           origin='lower', cmap='nipy_spectral',
    extent = [min(b1), max(b1), min(b2), max(b2)],
             vmax = abs(C).max(), vmin = -abs(C).max()
    )
    plt.plot(B0[0], B0[1], 'ro') #start point
    plt.text(B0[0] - .2, B0[1] + 0.8, 'start', fontsize = 14)

    plt.plot(p[0], p[1], 'ro') #stop point
    plt.text(p[0] - .2, p[1] + 0.8, 'stop', fontsize = 14)

    plt.text(-58,23,'steps = %d' %steps, fontsize=10)

random.seed(int(round(time.time() * 1000)))

begin = time.time()
(m,steps,trace) = minimize(Cost, B0, LEARNING_RATE, h, PRECISION)
end = time.time()

heatmap(Cost, trace)

show()

