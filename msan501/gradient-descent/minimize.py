
import numpy as np
from pylab import imshow, plot

def minimize(f, B0, eta, h, precision):
    trace = []
    B = np.array(B0)
    steps = 0
    while True:
        if steps % 10 == 0:  # only capture every 10th value
            trace.append(B)
        steps += 1

        finite_diff = np.array([f([B[0]+h, B[1]]) - f(B), f([B[0], B[1]+h]) - f(B)], dtype = float)
        B_new = B - eta * finite_diff


        if abs(B_new[0] - B[0]) < precision and abs(B_new[1] - B[1]) < precision :
                break

        B = B_new

    return (B, steps, trace)


