from collections import deque
d = deque([1,2,3])
d.extend([4,5])
d.extendleft([-2,7])
print(d)
d.rotate(-1)
print(d)


a = [1,1,2,3,4,1,3,4,5]
x=[i for i in a if i!=1 ] + [i for i in a if i==1]
print(x)