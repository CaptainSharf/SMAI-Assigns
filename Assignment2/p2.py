import numpy as np
import random
import matplotlib.pyplot as plt
from fileread import training_data
from fileread import size
from plot_data import plot_data_points

def voted_perceptron(dataset,num_epochs): #dataset is normalized
	w = np.array([0 for i in range(size)]+[0])
	count = 1
	ans = []
	for i in range(num_epochs):
		for j in range(len(dataset)):
			if np.dot(w,dataset[j][0])<=0:
				ans.append((w,count))
				w = w + dataset[j][0]
				count = 1
			else:
				count+=1
	ans.append((w,count))
	return ans

def perceptron(dataset):
	w = np.array([0 for i in range(size)]+[0]) #Initial w
	lerng_rate = 1 #eta=1
	max_num_itrns = 10000 #max itrns to conclude data is not linearly seperable
	num_itrns = 0
	size_data = len(dataset)
	k=0
	for i in range(max_num_itrns):
		j = 0
		while j<size_data and np.dot(w,dataset[j][0])>0:
			j+=1
		if j<size_data:
			w=w+(lerng_rate*dataset[j][0])
		else:
			num_itrns = i
			break
		k+=1
	return [w,num_itrns]

first_data = []
for ele in training_data:
	if ele[1]==1:
		first_data.append(ele)
	if ele[1]==2:
		first_data.append((-ele[0],-1))
val  = voted_perceptron(first_data,20)
sum_count = 0
temp = np.array([0 for i in range(size)]+[0])
for ele in val:
	temp = temp+ele[0]
	sum_count = sum_count+ele[1]
temp = temp/sum_count

print(temp)