import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
start_time = time()
features_train, features_test, labels_train, labels_test = preprocess()
end_time = time()
print(end_time-start_time)


start_time = time()
from sklearn.externals import joblib
model = joblib.load('model.pkl')
prd = model.predict([features_test[0]])
print(prd)

end_time = time()
print(end_time-start_time)


