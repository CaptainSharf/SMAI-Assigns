import numpy as np
import random

cont_vars = [0,5,16,17,18,24,29,38,40]
with open("census/census-income.data") as f:
	content  = f.readlines()
data1 = [lines.strip('.').split(',') for lines in content]
with open("census/census-income.test") as f1:
	content1 = f1.readlines()
data2 = [lines.strip().split(',') for lines in content1]
f.close()
f1.close()
list_dict = [{} for i in range(41)]
num_cl1 = 0
num_cl2 = 0

for ele in data1:
	for i in range(41):
		if i not in cont_vars and ele[i]!='?':
			temp_dict  = list_dict[i]
			if ele[i] not in temp_dict:
				list_dict[i][ele[i]]=[1,1]
			temp_dict = list_dict[i]
			if '-' in ele[41]:
				temp_dict[ele[i]][0]+=1
			else:
				temp_dict[ele[i]][1]+=1
	if '-' in ele[41]:
		num_cl1+=1
	else:
		num_cl2+=1

print(num_cl1,num_cl2,len(data1))