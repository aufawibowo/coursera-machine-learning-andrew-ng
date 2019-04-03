import numpy as np
import matplotlib.pyplot as plt

#def main():
#==========================================================================PART.2 PLOTTING
print('Plotting Data ...\n')
data = np.genfromtxt("ex1data1.txt", delimiter=",")
y=data[:,0]
x=data[:,1]
 
#m = length(y) #number of training examples

#Plot Data
# Note: You have to complete the code in plotData.m
#plotData(x, y)


#def plotData(x,y):
plt.scatter(y,x, color='red')
plt.ylabel('Profit in $10,000s')
plt.xlabel('Population of City in 10,000s')

#==========================================================================PART.3 GRADIENT DESCENT
print("Gradient Descent\n")
x=np.array([[tempx],[np.ones(x.shape)]],dtype=float)
theta=np.zeros((2,1),dtype=int)

iterations=1500
alpha=0.01

def gradientDescent(x,y,theta):
    m = y.shape
    J_history = np.zeros((iterations,1),dtype=int)
    for i in range(1,iterations):
        J_history(iter) = computeCost(x, y, theta)

def computeCost(x,y,theta):
    m = y.shape
    J = 0
    h=x*theta
    sqrErrors=np.power(h-y,2)
    J=1/(2*m)*np.sum(sqrErrors)
    return 





#if __name__ == '__main__':
#    main()
