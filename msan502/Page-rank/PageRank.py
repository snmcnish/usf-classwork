
import pandas
import numpy as np
import sys

filename = sys.argv[1]
filename2  = sys.argv[2]

#read in data - must be a text file separated by spaces
data = pandas.read_csv(filename, sep =' ' , header = None)
#read in dataset of airport codes
codes = pandas.read_csv(filename2, sep =' ' , header = None)

#convert data to a numpy array
adj_m = np.array(data)
adj_m = adj_m.astype(int)

#get highest origin node value (column 1)
max_org = adj_m[:,0].max()

#get highest destination node value (column 2)
max_dest = adj_m[:,1].max()

#set n as the max of the nodes
n = (max(max_org, max_dest))

#create an nxn zero matrix
A = np.zeros((n,n))

#put ones in A of the i,j index of origin and destination nodes
for row in adj_m:
    A[row[1] - 1, row[0] - 1] = 1

#loop through columns of A and divide by sum of each column to get the column
#stochastic transition matrix A
for i in range(0,n):
    if  sum(A[:,i]) != 0 :
        A[:,i] = A[:,i] / sum(A[:,i])
    else:
        A[:,i] = 0
    
#set p 
p = 0.15

#set B
B = np.ones((n,n)) * 1/float(n)

#calculate M, the google Matrix
M = A * (1-p) + p * B

#compute page rank vaceotr

#set v as a vector of uniform ditributions
v = np.ones(n) * 1/float(n)

#calculate M^k*v

pagerank = v   #set initial pagerank value as v
k = 100   #set k value

for k in range (0,k+1):   
    prev = pagerank  #each time the loop executes, set prev as the old pagerank value
    
    if k == 0:  
        Mk = np.dot(M,M)   #multiply M times itself for the first iteration
    else:
        Mk = np.dot(Mk,M)  #multiply M with the previous M^k
    
    pagerank = np.dot(Mk,v)  #calculate pagerank by multiplying M^k*v
    
print k, pagerank
print k-1 , prev

#check if k was big enough

precision = np.ones(n)*.00001 #set precision values

diff= abs(np.subtract(pagerank, prev)) #subtract the pagerank vector from the previous to see if it has converged

if (diff < precision).all() == True:    #compare the difference to a precision value
    print "The page rank value converged at your chosen k"
else:
    print "Choose a larger k"
    
#create an array of the pages and pagerank values
pages = np.array(range(1, n+1)).astype(int)
pagerank_sol = np.column_stack((pages,pagerank)) 

#merge page rank vector with meta data
pagerank_sol = pandas.DataFrame(pagerank_sol) #convert pagerank vector to data frame
pagerank_sol.columns = ['node', 'score']    #name columns
codes.columns = ['node', 'code']            #name columns

pagerank_sol = pandas.merge(pagerank_sol, codes, how='left', on = 'node')   #merge on ndoe

#sort pagerank 

pagerank_sol_sort =  pagerank_sol.sort_values(by = 'score', ascending= False)

#top 10 
top10 =  pagerank_sol_sort[:10]
print "The highest ranking nodes are:"
print top10

#bottom 10
bottom10 = pagerank_sol_sort[-10:]
print "The least ranking nodes are:"
print bottom10