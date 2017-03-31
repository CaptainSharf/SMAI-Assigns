from numpy import array, dot, random
import numpy as np
import math

def sigmoid(x):
    return 1.0/(1 + math.exp(-x))

f = open('optdigits-orig.wdep', 'r')
lines = f.readlines()
f.close()

imagesOf1 = []
imagesOf2 = []
imagesOf3 = []
allimages = []
mapp = []
image = ''
for line in lines:
    if len(line.strip('\n')) == 32:
        image += line + '\n'
    else:
        number = line.strip('\n').strip()
        if number == '1' or number == '2' or number == '3':
            tempImage = image.split('\n')
            tempImage = filter(None, tempImage)
            tempImageArray = []
            for i in tempImage:
                arrays = list(i)
                tempImageArray.append(arrays)
            if number == '1':
                imagesOf1.append(tempImageArray)
                mapp.append(1)
            if number == '2':
                imagesOf2.append(tempImageArray)
                mapp.append(2)
            if number == '3':
                imagesOf3.append(tempImageArray)
                mapp.append(3)
            allimages.append(tempImageArray)
            image = ''
        else:
            image = ''

weights = random.rand(65, 10)
hidden_weights = random.rand(10,3)
expectedFor1 = array([0, 1,0])
expectedFor2 = array([1, 0,0])
expectedFor3 = array([1, 1,1])
eta = 0.2

for _ in range(2000):
    for ppp in range(len(allimages)):
        new_matrix = [[0 for i in range(8)] for j in range(8)]
        rows = 0
        columns = 0
        for i in range(0, 32, 4):
            for j in range(0, 32, 4):
                average = 0
                for k in range(i, i + 4):
                    for l in range(j, j + 4):
                        average += int(allimages[ppp][k][l])
                new_matrix[rows][columns] = average/16.0
                columns += 1
            rows += 1
            columns = 0
        
        newImageArray = array([new_matrix[i][j] for i in range(8) for j in range(8)] + [1])
        netj = dot(newImageArray[np.newaxis], weights)
        # temp = newImageArray
    
        yj = []
        for i in netj:
            for j in range(len(i)):
                yj.append(sigmoid(i[j]))
        
        netk = dot(array(yj), hidden_weights)
    
        zk = []
        for i in netk[np.newaxis]:
            for j in range(len(i)):
                zk.append(sigmoid(i[j]))

        if mapp[ppp]==1:
            tk_zk = expectedFor1 - array(zk)[np.newaxis]
        elif mapp[ppp]==2:
            tk_zk = expectedFor2 - array(zk)[np.newaxis]
        else:
            tk_zk = expectedFor3 - array(zk)[np.newaxis]
        
        fdashofnetk = []
        for i in netk[np.newaxis]:
            for j in range(len(i)):
                fdashofnetk.append(sigmoid(i[j])*(1 - sigmoid(i[j])))
        
        deltak = np.multiply(tk_zk, array(fdashofnetk)[np.newaxis])
        sigma = dot(hidden_weights, deltak.T)
        fdashofnetj = []
        for i in netj:
            for j in range(len(i)):
                fdashofnetj.append(sigmoid(i[j])*(1 - sigmoid(i[j])))
        sumy = dot(hidden_weights, deltak.T)
    
        deltaj = np.multiply(array(fdashofnetj)[np.newaxis], sumy.T)
        
        weights += eta * dot(newImageArray[np.newaxis].T, deltaj)
        hidden_weights += eta * dot(array(yj)[np.newaxis].T, deltak)
        #print weights
        #print '----------------------------------------------'
        #print hidden_weights
        print(zk,mapp[ppp])
#print(lines)