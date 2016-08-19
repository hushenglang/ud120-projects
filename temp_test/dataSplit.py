# import numpy
# from sklearn import datasets
# from sklearn import cross_validation
#
# iris = datasets.load_iris()
# x_train, y_train, x_test, y_test = cross_validation.train_test_split(iris.data, iris.target, train_size=0.9, random_state=0)
# print x_train.shape
# print y_train.shape
#
# #
# #
# # print iris.data
# #
# # print iris.keys()
# # print iris['feature_names']
# # print iris.target


from sklearn import datasets
from sklearn.svm import SVC

iris = datasets.load_iris()
features = iris.data
labels = iris.target

###############################################################
### YOUR CODE HERE
###############################################################

### import the relevant code and make your train/test split
### name the output datasets features_train, features_test,
### labels_train, and labels_test

### set the random_state to 0 and the test_size to 0.4 so
### we can exactly check your result
from sklearn import cross_validation
features_train, labels_train, features_test, labels_test = cross_validation.train_test_split(features, labels, test_size=0.4, random_state=0)
print features_train.shape
print labels_train.shape

print features_test.shape
print labels_test.shape


###############################################################

# clf = SVC(kernel="linear", C=1.)
# clf.fit(features_train, labels_train)
#
# # print clf.score(features_test, labels_test)
#
#
# ##############################################################
# def submitAcc():
#     return clf.score(features_test, labels_test)