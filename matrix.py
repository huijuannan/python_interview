# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Solve following funcction step by step using Cramer's rule:
y = w0 + w1 * x1 + w2 * x2 + w3 * x3
'''
import numpy as np
data = np.genfromtxt('data.csv',delimiter=',',skiprows=1)
x1=data[:,0]
x2=data[:,1]
x3=data[:,2]
y=data[:,3]

# calculate sum and sum of square for each variable
sum_x1= np.sum(x1)
sum_x1_square = np.sum(np.square(x1))

sum_x2= np.sum(x2)
sum_x2_square = np.sum(np.square(x2))

sum_x3= np.sum(x3)
sum_x3_square = np.sum(np.square(x3))

sum_y = np.sum(y)

# calculate covariance between two variables
sum_x1_x2 = np.sum(x1*x2)
sum_x1_x3 = np.sum(x1*x3)
sum_x1_y = np.sum(x1*y)
sum_x2_x3 = np.sum(x2*x3)
sum_x2_y = np.sum(x2*y)
sum_x3_y = np.sum(x3*y)
n = np.shape(y)[0]

#form the column of coefficient matrix
cY = np.array([[sum_y, sum_x1_y, sum_x2_y, sum_x3_y]]).T
cW0 = np.array([[n, sum_x1, sum_x2, sum_x3]]).T
cW1 = np.array([[sum_x1, sum_x1_square, sum_x1_x2, sum_x1_x3]]).T
cW2 = np.array([[sum_x2, sum_x1_x2, sum_x2_square, sum_x2_x3]]).T
cW3 = np.array([[sum_x3, sum_x1_x3, sum_x2_x3, sum_x3_square]]).T

# coefficient matrix
W0 = np.hstack((cY, cW1, cW2, cW3))
W1 = np.hstack((cW0, cY, cW2, cW3))
W2 = np.hstack((cW0, cW1, cY, cW3))
W3 = np.hstack((cW0, cW1, cW2, cY))
Y = np.hstack((cW0, cW1, cW2, cW3))

# calculate the parameters by deviding the determinants
w0 = np.linalg.det(W0)/np.linalg.det(Y)
w1 = np.linalg.det(W1)/np.linalg.det(Y)
w2 = np.linalg.det(W2)/np.linalg.det(Y)
w3 = np.linalg.det(W3)/np.linalg.det(Y)