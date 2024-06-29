a = [1,2,3,4,5,]
b =['a','b','c','b','e']

for x , y in zip(a,b):
    print(x,y)

c = zip(a,b)
d = list(c)
print(d)


def fibb():
    a,b= 0,1
    while True:
        yield a
        a,b = b ,a+b

obj = fibb()
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))


def fibb(n):
    a,b= 0,1
    for _ in range(n):
        yield a
        a,b = b ,a+b

for i in fibb(10):
    print(i)