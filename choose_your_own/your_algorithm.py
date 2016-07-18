#!/usr/bin/python
print "start"

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()

print "finish preparing data"

### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]

print "build plot data"
print grade_fast
print bumpy_fast
print grade_slow
print bumpy_slow

#### initial visualization
# plt.xlim(0.0, 1.0)
# plt.ylim(0.0, 1.0)
# plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
# plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
# plt.legend()
# plt.xlabel("bumpiness")
# plt.ylabel("grade")
# # plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

print "start create classifier"

### this is nearset neighbors algorithm.
from sklearn import neighbors
# clf = neighbors.KNeighborsClassifier(n_neighbors=15, weights='distance')
# clf.fit(features_train, labels_train)
# prd = clf.predict(features_test)

# clf = neighbors.RadiusNeighborsClassifier(radius=1.0, weights='distance')
# clf.fit(features_train, labels_train)
# prd = clf.predict(features_test)



###adaboost algorithm
from sklearn.ensemble import AdaBoostClassifier
clf = AdaBoostClassifier(n_estimators=50)
clf.fit(features_train, labels_train)
prd = clf.predict(features_test)



from sklearn.metrics import accuracy_score

acc = accuracy_score(labels_test, prd)
print acc




try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
