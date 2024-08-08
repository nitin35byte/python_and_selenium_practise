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

def nested_sum(n):
    sum = 0
    for i in n:
        if type(i) == list:
            sum += nested_sum(i)
        else:
            sum += i
    return sum
n = (1,2,3,[1,2,3],8,[3,4])
l = nested_sum(n)
print(l)