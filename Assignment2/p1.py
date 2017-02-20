import numpy as np
import random
from plot_data import plot_data_points

training_data = [(np.array([0.1,1.1,1]),1),(np.array([7.1,4.2,1]),2),(np.array([-3,-2.9,1]),3),
(np.array([6.8,7.1,1]),1),(np.array([-1.4,-4.3,1]),2),(np.array([0.5,8.7,1]),3),
(np.array([-3.5,-4.1,1]),1),(np.array([4.5,0,1]),2),(np.array([2.9,2.1,1]),3),
(np.array([2.0,2.7,1]),1),(np.array([6.3,1.6,1]),2),(np.array([-0.1,5.2,1]),3),
(np.array([4.1,2.8,1]),1),(np.array([4.2,1.9,1]),2),(np.array([-4.0,2.2,1]),3),
(np.array([3.1,5,1]),1),(np.array([1.4,-3.2,1]),2),(np.array([-1.3,3.7,1]),3),
(np.array([-0.8,-1.3,1]),1),(np.array([2.4,-4,1]),2),(np.array([-3.4,6.2,1]),3),
(np.array([0.9,1.2,1]),1),(np.array([2.5,-6.1,1]),2),(np.array([-4.1,3.4,1]),3),
(np.array([5,6.4,1]),1),(np.array([8.4,3.7,1]),2),(np.array([-5.1,1.6,1]),3),
(np.array([3.9,4,1]),1),(np.array([4.1,-2.2,1]),2),(np.array([1.9,5.1,1]),3)]



def perceptron(dataset):
	w = np.array([0,0,0]) #Initial w
	lerng_rate = 1 #eta=1
	max_num_itrns = 10000 #max itrns to conclude data is not linearly seperable
	num_itrns = 0
	size_data = len(dataset)
	for i in range(max_num_itrns):
		j = 0
		while j<size_data and np.dot(w,dataset[j][0])>0:
			j+=1
		if j<size_data:
			w=w+(lerng_rate*dataset[j][0])
		else:
			num_itrns = i
			break
	return [w,num_itrns]


first_data = []
second_data = []
for elmnt in training_data:
	if elmnt[1]==1:
		first_data.append(elmnt)
	if elmnt[1]==2:
		first_data.append((-elmnt[0],-1))
		second_data.append(elmnt)
	if elmnt[1]==3:
		second_data.append((-elmnt[0],-1))
[a,num_itrns1] = perceptron(first_data)
[w,num_itrns2] = perceptron(second_data)
plot_data_points(second_data,w,2,3)
plot_data_points(first_data,a,1,2)
print (num_itrns1,num_itrns2)