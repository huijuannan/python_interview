# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Use two different method to derive the parameters of following funcction:
y = w0 + w1 * x1 + w2 * x2 + w3 * x3
1. Least linear square: w = linRegress(x,y)
Using QR decomposition of matrix

2. Stochastic Gradient Descent: w = sgd(x,y, alpha = 0.001,iteration=200)
alpha: learning rate, default is 0.001
iteration: iteration time, default is 100

'''
import numpy as np

def linRegress(x,y):
	sampleNum = len(y)
	X = np.hstack((np.ones((sampleNum,1)), x))	
	q, r = np.linalg.qr(X) # QR decoposition
	p = np.dot(q.T,y)
	w = np.dot(np.linalg.inv(r),p)
	return w,  rmse(y, np.dot(X,np.array([w]).T))


def sgd(x,y, alpha = 0.001,iteration=100):
	sampleNum = len(y)
	x = np.hstack((np.ones((sampleNum,1)), x))
	varNum = x.shape[1]
	# initialize the parameters
	w = 2*np.random.random((varNum,1)) - 1

	for i in xrange(iteration):
		for j in xrange(sampleNum): # w updata with each sample
			y_estimated = np.dot(x[j], w)
			y_error = (y_estimated - y[j])*np.ones((1,varNum))
			w_delta = alpha*y_error*x[j] 
			w = w - w_delta.T
	return w.squeeze(), rmse(y, np.dot(x,w))

def rmse(yt,y):
	return np.sqrt(((yt - y) ** 2).mean())


def Main():
	data = np.genfromtxt('data.csv',delimiter=',',skiprows=1)
	x = data[:,:3]
	y = data[:,3]
	w_lin, rmse_lin = linRegress(x,y)
	w_sgd, rmse_sgd = sgd(x,y)
	print 'function: y = w0 + w1 * x1 + w2 * x2 + w3 * x3'
	print 'Solution with matrix algorithm:'
	print 'w0={0:03.3f}, w1={1:03.3f}, w2 = {2:03.3f}, w3 = {3:03.3f}'.format(*w_lin)
	print 'RMSE = {rmse:03.3f}'.format(rmse=rmse_lin)
	print 'Solution using Stochastic Gradient Descent:'
	print 'w0={0:03.3f}, w1={1:03.3f}, w2 = {2:03.3f}, w3 = {3:03.3f}'.format(*w_sgd.T)
	print 'RMSE = {rmse:03.3f}'.format(rmse=rmse_sgd)


if __name__ == "__main__":
	Main()
