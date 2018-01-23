import sys
from PIL import Image

# define your flip function here

def flip(img):

    width, height = img.size

    imgdup = img.copy()

    m_img = img.load()
    m_imgdup = imgdup.load()

    for x in range(0,width):
        for y in range(0,height):

            m_imgdup[(x,y)] = m_img[(width-x-1,y)]

    return imgdup




if len(sys.argv)<=1:
	print "missing image filename"
	sys.exit(1)
filename = sys.argv[1]
img = Image.open(filename)
img = img.convert("L")
img.show()

# call your flip function here

img = flip(img)

img.show()
