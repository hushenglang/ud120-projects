import time
t0 = time.time()
print t0


a = [0, 0, 1, 1, 1, 0, 0]

print len([a[i] for i in range(0, len(a)) if a[i]==1])