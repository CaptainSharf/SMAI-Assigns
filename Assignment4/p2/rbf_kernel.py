import numpy as np
from sklearn import svm
from plot_data import data_cl1,data_cl2,x1,x2,y1,y2
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt 

training_data = data_cl1+data_cl2
label = [1]*len(data_cl1)+[-1]*len(data_cl2)

final_C = 0
final_deg = 0
max_score = 0
crs_val_mean = []
crs_val_std = []
for i in np.arange(1,3,0.5):
	for j in range(1,7):
		clf = svm.SVC(C=i,kernel = 'poly',gamma=j)
		scores = cross_val_score(clf,training_data,label,cv=10)
		if sum(scores)>max_score:
			final_C = i
			final_deg = j
			max_score = sum(scores)

clf = svm.SVC(C=final_C,kernel = 'rbf',gamma=final_deg)

for i in range(30):
	scores = cross_val_score(clf,training_data,label,cv=10);
	crs_val_mean.append(np.mean(np.array(scores)))
	crs_val_std.append(np.std(np.array(scores)))

clf = svm.SVC(C=1,kernel='rbf', gamma=2)
clf.fit(training_data, label)

# plot the line, the points, and the nearest vectors to the plane
plt.figure(1, figsize=(4,3))
plt.clf()

plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=80,
            facecolors='none', zorder=10)
plt.scatter(x1+x2, y1+y2, c=label, zorder=10, cmap=plt.cm.Paired)

plt.axis('tight')
x_min = -2
x_max = 2
y_min = -2
y_max = 2

XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
Z = clf.decision_function(np.c_[XX.ravel(), YY.ravel()])

# Put the result into a color plot
Z = Z.reshape(XX.shape)
plt.figure(1, figsize=(4, 3))
plt.pcolormesh(XX, YY, Z > 0, cmap=plt.cm.Paired)
plt.contour(XX, YY, Z, colors=['k', 'k', 'k'], linestyles=['--', '-', '--'],
            levels=[-.5, 0, .5])

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
print(final_deg,final_C)
plt.xticks(())
plt.yticks(())
plt.show()
x = [i for i in range(30)]
plt.plot(x,crs_val_mean,'b')
plt.plot(x,crs_val_std,'r')
plt.show()