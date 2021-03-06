#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

print type(features)

### it's all yours from here forward!
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

from sklearn.metrics import accuracy_score
print accuracy_score(labels_test, prd)
