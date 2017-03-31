import numpy as np
import random
from preproc import *
from math import log,log2

def predict(ele):
	sum_1 = 0
	sum_2 = 0
	for i in range(41):
		if i not in cont_vars or ele[i]!='?' and ele[i] in list_dict[i]:
			vals = list_dict[i][ele[i]]
			sum_1 = sum_1+log2(vals[0]/sum(vals))
			sum_2 = sum_2+log2(vals[1]/sum(vals))
	sum_1 = sum_1+log2(num_cl1)
	sum_2 = sum_2+log2(num_cl2)
	if sum_1>sum_2:
		return 1
	else:
		return 2

def label(ele):
	if '-' in ele[41]:
		return 1
	else:
		return 2

correct = 0
for ele in data2:
		if predict(ele)==label(ele):
			correct+=1
print(len(data2))