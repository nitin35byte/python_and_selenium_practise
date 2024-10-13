import random

l ={"apple" , "banana"  ,"apple"}
print(l)
print(type(l))
#l.clear()
#print(l)
l.add("guava")
print(l)
l ='nitib'
p="".join(reversed(l))
print(p)


num= random.randint(1 , 100)
print(num)

num= random.randrange(1 , 100 , 2)
print(num)

num= random.sample(range(1 , 100) ,3)
print(num)