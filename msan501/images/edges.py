from filter import *

def laplace(data):

    return sum(data[1:5]) - (4*data[0])


img = open(sys.argv)
img.show()
edges = filter(img, laplace)
edges.show()