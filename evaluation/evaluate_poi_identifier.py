#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
import numpy as np
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.3, random_state=42)
print np.array(features_train).shape
print np.array(features_test).shape
print np.array(labels_train).shape
print np.array(labels_test).shape

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)
prd = clf.predict(features_test)
print 'labels_test:', labels_test
print 'prd: ', prd

from sklearn.metrics import accuracy_score
print 'accuracy: ', accuracy_score(labels_test, prd)

from sklearn.metrics import recall_score
print 'recall score: ', recall_score(labels_test, prd)

from sklearn.metrics import precision_score
print 'precision score:', precision_score(labels_test, prd)

poiList = [labels[i] for i in range(0,len(labels_test)) if labels[i]==1]
print 'POI numbers:', len(poiList)
print 'total numbers:', len(labels_test)

