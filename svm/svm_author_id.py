#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
features_train = features_train[:len(features_train)/1]
labels_train = labels_train[:len(labels_train)/1]


#########################################################
### your code goes here ###
from sklearn.svm import SVC
t0 = time()
clf = SVC(kernel='rbf', C=10000)
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

prd = clf.predict(features_test)
print "predict time:", round(time()-t0, 3), "s"

print prd

print "chris maile count: ", len([prd[i] for i in range(0, len(prd)) if prd[i]==1])

from sklearn.metrics import accuracy_score
score = accuracy_score(labels_test, prd)
print score
#########################################################
##predict only emlement number 10, 26 and 50
# r1 = clf.predict([features_test[10]])
# r2 = clf.predict([features_test[26]])
# r3 = clf.predict([features_test[50]])
# print r1, r2, r3


