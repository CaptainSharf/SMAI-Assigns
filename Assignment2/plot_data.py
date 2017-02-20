import matplotlib.pyplot as plt
import numpy as np 

def plot_data_points(dataset,w,cl1,cl2):
	x_red_data = []
	y_red_data = []
	x_blue_data = []
	y_blue_data = []
	for ele in dataset:
		if ele[1]==cl1:
			x_red_data.append(ele[0][0])
			y_red_data.append(ele[0][1])
		else:
			x_blue_data.append(-ele[0][0])
			y_blue_data.append(-ele[0][1])
	plt.plot(x_red_data,y_red_data,'ro')
	plt.plot(x_blue_data,y_blue_data,'bo')
	x_axis = np.array([min(min(x_blue_data,x_red_data))-1,max(max(x_blue_data,x_red_data))+1])
	y_axis = [min(min(y_red_data),min(y_blue_data))-1,max(max(y_blue_data),max(y_red_data))+1]
	plt.axis([min(min(x_blue_data),min(x_red_data))-1,max(max(x_blue_data),max(x_red_data))+1,
		min(min(y_red_data),min(y_blue_data))-1,max(max(y_blue_data),max(y_red_data))+1])
	[a,b,c]= w
	y = ((-a)*x_axis+(-c))/b
	plt.plot(x_axis,y,'r--')
	plt.show()