#import necessary libraries
import sys
from PIL import Image
import numpy as np
from scipy.misc import toimage
import matplotlib.pyplot as plt



def mySVD(filename, k):

	#open image for each filename
	img = Image.open(filename)

	#convert to greyscale
	img = img.convert("L")

	#display the image
	img.show()

	#load image into matrix
	A = np.asarray(img.getdata(), dtype = 'float').reshape((img.size[1], img.size[0]))

	#compute A transpose * A
	AtA = np.dot(np.transpose(A), A)

	#find eigenvectors and eigenvalues
	w1, v = np.linalg.eig(AtA)

	#find s (square root of eigenvalues)
	s =  np.sqrt(w1)
	s = np.array(s)

	#put s's on end of eigenvectors of AtA
	v_s = np.column_stack((v,s))

	#sort by s
	v_s_sort = v_s[np.lexsort((v_s[:,0],v_s[:,-1]))]
	v_s_sort = v_s_sort[::-1] #reverse sort

	#remove s from last column
	v_sort = np.delete(v_s_sort, -1, axis=1)

	###find s

	#get sorted s
	s_sort = v_s_sort[:,-1]
	s = s_sort

	###find V

	#fill the V matrix with columns representing the normalized eigenvectors of AtA

	V = np.transpose(v_sort)

	###find U

	#U is A*v divided by the sigmas for each column

	U = np.empty((m,n))

	Av = np.dot(A, v_sort)

	U = Av/s

	###compute the SVD by iterating through U*s*V k times

	A_new = np.zeros((m,n))

	for i in range(0,k):
		Us = U[:,i] * s[i]
		Ak = np.outer(Us,V[i,:])
		A_new = A_new + Ak

	#display new image
	img = Image.fromarray(A_new)

	img.show()

	return s


#check for script parameters
if len(sys.argv)<=1:
	print "missing image filename"
	sys.exit(1)

##PART A
#get k (first element of your script parameters)
k_choice = int(sys.argv[1])

#import dogs collection images (first 10 arguments of script parameters)
#dog pics are 720 x 720
files = sys.argv[2:12]

#get m and n for use in below arguments below by opening fiesrt file in the collection
img = Image.open(sys.argv[2])
img = img.convert("L")
A = np.asarray(img.getdata(), dtype='float').reshape((img.size[1], img.size[0]))

n = A.shape[0]
m = A.shape[1]

#call SVD function for all dog images
s_dogs = np.empty((n, len(files)))
for i in range(0,len(files)):
	filename = files[i]
	s_dogs[:,i]= mySVD(filename, k = k_choice)  #choose k here!

#compute average s of the collection of images
s_average_d = np.apply_along_axis(np.mean, 1, s_dogs)


#import potraits collection images (second 10 arguments of script parameters)
#portrait pics are 720 x 720
files = sys.argv[12:22]

#call SVD function for all portrait images
s_port = np.empty((n, len(files)))
for i in range(0,len(files)):
	filename = files[i]
	s_port[:,i]= mySVD(filename, k = k_choice)  #choose k here!

#compute average of the collection of images
s_average_p = np.apply_along_axis(np.mean, 1, s_port)


#create 10 random greyscale images and save in working directory
#will be of same number and size as used above
for i in range(0,len(files)):
	width, height = m, n
	array = (np.random.rand(width*height) < 0.5).astype(int)
	array = array.reshape(height, width)
	im = toimage(array)
	im.save("random" + str(i) + ".png")


#import random collection images (third 10 arguments of script parameters
#portrait pics are 720 x 720
files = sys.argv[22:34]

#call SVD function for all random images
s_rand = np.empty((n, len(files)))
for i in range(0,len(files)):
	filename = files[i]
	s_rand[:,i]= mySVD(filename, k_choice)  #choose k here!

#compute average of the collection of images
s_average_r = np.apply_along_axis(np.mean, 1, s_rand)


#compare singular values

##plot singular values for dog collection

plt.figure(1)
plt.scatter(range(0,len(s_average_d)), s_average_d , alpha = 0.6)
plt.title("Average Singular Values Dogs Collection")
plt.xlabel("Index")
plt.ylabel("Singular Value")
plt.savefig('dogsplot.png')
plt.show()

# ##plot singular values for portrait collection

plt.figure(2)
plt.scatter(range(0,len(s_average_p)), s_average_p, alpha = 0.6)
plt.title("Average Singular Values Portraits Collection")
plt.xlabel("Index")
plt.ylabel("Singular Value")
plt.savefig('portraitplot.png')
plt.show()

# ##plot singular values for random collection

plt.figure(3)
plt.scatter(range(0,len(s_average_r)), s_average_r, alpha = 0.6)
plt.title("Average Singular Values of Random Greyscale Image")
plt.xlabel("Index")
plt.ylabel("Singular Value")
plt.savefig('ranomplot.png')
plt.show()



##PART B

#make m and in floats so they can be used in ratio division
m = float(m)

#compression ratio

##dogs collection
#too messy
k = 1
compression = ((m+n)*k)/(m*n) #compute compression ratio
print round(compression,3)
ratio = sum(s_average_d[0:k]) / sum(s_average_d[0:n]) #total mass of the singular values before k /total mass of the entire singular values
print round(ratio,3)

#slightly messy
k = 50
compression = ((m+n)*k)/(m*n) #compute compression ratio
print round(compression,3)
ratio = sum(s_average_d[0:k]) / sum(s_average_d[0:n]) #total mass of the singular values before k /total mass of the entire singular values
print round(ratio,3)

#indistinguishable
k = 350
compression = ((m+n)*k)/(m*n) #compute compression ratio
print round(compression,3)
ratio = sum(s_average_d[0:k]) / sum(s_average_d[0:n]) #total mass of the singular values before k /total mass of the entire singular values
print round(ratio,3)

##portrait collection
#too messy
k = 1
compression = ((m+n)*k)/(m*n) #compute compression ratio
print round(compression,3)
ratio = sum(s_average_p[0:k]) / sum(s_average_p[0:n]) #total mass of the singular values before k /total mass of the entire singular values
print round(ratio,3)

#slightly messy
k = 50
compression = ((m+n)*k)/(m*n) #compute compression ratio
print round(compression,3)
ratio = sum(s_average_p[0:k]) / sum(s_average_p[0:n]) #total mass of the singular values before k /total mass of the entire singular values
print round(ratio,3)

#indistinguishable
k = 350
compression = ((m+n)*k)/(m*n) #compute compression ratio
print round(compression,3)
ratio = sum(s_average_p[0:k]) / sum(s_average_p[0:n]) #total mass of the singular values before k /total mass of the entire singular values
print round(ratio,3)


##PART C

# #log log plot for dogs collection
# take log of average values of s
y =  np.log(s_average_d)
x =  np.log(np.array(range(1,len(s_average_d)+1)))

fig = plt.figure(4)
ax=plt.gca()
ax.scatter(x, y, alpha = 0.6)
plt.title("Log Log Plot of Average Singular Values of Dogs Collection")
plt.xlabel("Log(Index)")
plt.ylabel("Log(Singular Value)")
plt.savefig('doglogplot.png')
plt.show()

# #log log plot for portrait collection
# take log of average values of s
y =  np.log(s_average_p)
x =  np.log(np.array(range(1,len(s_average_p)+1)))

fig = plt.figure(5)
ax=plt.gca()
ax.scatter(x, y, alpha = 0.6)
plt.title("Log Log Plot of Average Singular Values of Portraits Collection")
plt.xlabel("Log(Index)")
plt.ylabel("Log(Singular Value)")
plt.savefig('portlogplot.png')
plt.show()


# #log log plot for random greyscale collection
# take log of average values of s
y =  np.log(s_average_r)
x =  np.log(np.array(range(1,len(s_average_r)+1)))

fig = plt.figure(6)
ax=plt.gca()
ax.scatter(x, y, alpha = 0.6)
plt.title("Log Log Plot of Average Singular Values of Random Greyscale Collection")
plt.xlabel("Log(Index)")
plt.ylabel("Log(Singular Value)")
plt.savefig('ranomlogplot.png')
plt.show()



