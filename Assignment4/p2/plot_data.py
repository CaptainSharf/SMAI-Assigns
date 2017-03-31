import numpy as np
import random
import matplotlib.pyplot as plt
import csv

data_cl1 = []
data_cl2 = []
with open("Data_SVM.csv") as f:
	reader = csv.DictReader(f)
	for row in reader:
		if row['V3']=='1':
			data_cl1.append([float(row['V1']),float(row['V2'])] )
		else:
			data_cl2.append([float(row['V1']),float(row['V2'])])
x1 = []
y1 = []
for ele in data_cl1:
	x1.append(ele[0])
	y1.append(ele[1])
x2 = []
y2 = []
for ele in data_cl2:
	x2.append(ele[0])
	y2.append(ele[1])
# plt.scatter(x1, y1,color='red')
# plt.scatter(x2,y2,color='blue')
# plt.show()