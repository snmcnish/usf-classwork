import sys
from PIL import Image

# define your blur function here

def blur(img):
    width, height = img.size

    imgdup = img.copy()

    pixels = imgdup.load()

    for x in range(0,width):
        for y in range(0,height):
            r = region3x3(img, x, y)
            pixels[x,y] = avg(r)


    return imgdup



def avg(data):
    return sum(data)/len(data)


def region3x3(img, x, y):
    me = getpixel(img, x, y)
    N = getpixel(img, x, y - 1)
    NE = getpixel(img, x + 1, y - 1)
    E = getpixel(img, x + 1, y)
    SE = getpixel(img, x + 1, y + 1)
    S = getpixel(img, x, y + 1)
    SW = getpixel(img, x - 1, y + 1)
    W = getpixel(img, x - 1, y)
    NW = getpixel(img, x - 1, y - 1)

    return [me, N, S, E, W, NW, NE, SE, SW]

def getpixel(img, x, y):
    width, height = img.size
    if x < 0:
        x = 0
    if x >= width:
        x = width - 1
    if y < 0:
        y = 0
    if y >= height:
        y = height - 1

    imgdup = img.copy()
    pixels = imgdup.load()

    return pixels[(x,y)]

if len(sys.argv)<=1:
	print "missing image filename"
	sys.exit(1)
filename = sys.argv[1]
img = Image.open(filename)
img = img.convert("L")


img.show()

# call your blur function here

img = blur(img)


img.show()
