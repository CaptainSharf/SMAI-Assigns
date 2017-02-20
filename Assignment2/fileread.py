size = 4
fname = "./AllData/sensor_readings_4.data"
import numpy as np
with open(fname) as f:
    content = f.readlines()
content = [x.strip().split(',') for x in content]
training_data = []
keys = {}
key_val =1
for ele in content:
	arr = np.array([float(ele[i]) for i in range(size)]+[1])
	if ele[size] in keys:
		training_data.append((arr,keys[ele[size]]))
	else:
		keys[ele[size]] = key_val
		key_val+=1
	training_data.append((arr,keys[ele[size]]))
#print(keys)
#print (training_data)