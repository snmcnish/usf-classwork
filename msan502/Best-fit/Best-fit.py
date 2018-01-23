import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np



def bestfit(data):
    
    fr = pd.read_csv(data)
    

    #plot x and y to see if linear relationship is a reasonable assumption
    
    plt.plot(fr['x'], fr['y'], 'ro')
    plt.show()
    
    #my model
    
    y = fr.y #response
    X = fr.x #predictor
    
    A = np.array(sm.add_constant(X)) #add a contant term to the predictor
    
    Atrans = np.array(A.transpose()) #transpose A
    
    AAT = np.dot(Atrans,A) #get A * A^t
    ATB = np.dot(Atrans,y) #get A^t * b
    
    Xhat= np.dot(np.linalg.inv(AAT), ATB) #solve to get x hats
    print "The intercept of my model is : {0} ".format(Xhat[0])
    print "The slope of my model is : {0} ".format(Xhat[1])
    
    line = Xhat[0] + Xhat[1]*X #plug in x values to my best fit line
    
    sumsquares = np.linalg.norm(line - y)**2 #calculate sum of squares
    print "The sum of squares of the distances from the observed y-values to the y-values on my line is : {0}".format(sumsquares) 
    
    
    
    #get answer from statsmodels.ols to compare to
    
    y = fr.y #response
    X = fr.x #predictor
    X = sm.add_constant(X) #add a contant term to the predictor
    
    est = sm.OLS(y, X) #perform regression
    
    est = est.fit() #fit the model
    
    est.summary() #print results
    
    print "Using stasmodels.ols, the slope and interept are : {0}".format(est.params)

    return Xhat[0], Xhat[1], sumsquares


bestfit(data = '/Users/smcnish/classes/msan502/HW3/TVlife.txt')
        
bestfit(data = '/Users/smcnish/classes/msan502/HW3/population.txt')

bestfit(data = '/Users/smcnish/classes/msan502/HW3/nba.txt')

bestfit(data = '/Users/smcnish/classes/msan502/HW3/ny-avg-winter-temp.csv')
