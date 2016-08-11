""" quiz materials for feature scaling clustering """

### FYI, the most straightforward implementation might 
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!  
### why would you rescale it?  Or even use it at all?
def featureScaling(arr):
    tmax = max(arr)
    tmin = min(arr)
    res = []
    for i in range(0,len(arr)):
        x=arr[i]
        y=(x-tmin)/float((tmax-tmin))
        res.append(y)
    
    return res

# tests of your feature scaler--line below is input data
data = [[115.], [140.], [175.]]
# print featureScaling(data)



from sklearn.preprocessing import MinMaxScaler
import numpy
s = MinMaxScaler()
r = s.fit_transform(numpy.array(data))
print r

