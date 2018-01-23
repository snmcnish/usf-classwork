from filter import *

def laplace(data):

    return sum(data[1:5]) - (4*data[0])


# Return a new image whose pixels are A[x,y] - B[x,y]
def minus(A, B):

    width, height = A.size

    imgdup = A.copy()
    edges_img = B.copy()

    pixels_a = imgdup.load()
    pixels_b = edges_img.load()

    for x in range(0,width):
        for y in range(0,height):

            pixels_a[x,y] = pixels_a[x,y] - pixels_b[x,y]


    return imgdup


img = open(sys.argv)
img.show()
edges = filter(img, laplace)
sharpen = minus(img,edges)
sharpen.show()