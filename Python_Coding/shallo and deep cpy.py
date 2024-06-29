import copy

a = [1,2,[3,4,5],9,8]
b = copy.deepcopy(a)
print(b)
print(a)
print(id(a))
print(id(b))

b [1]=22
print(a)
print(b)


c = copy.copy(a)
print(id(c))
print(id(a))
print(a)
print(c)
c [2][0]=77
print(c)
print(a)