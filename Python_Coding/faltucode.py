a = [1,2,3,4,5,6]
for a[-1] in a:
    print(a[-1])

print(a)
a = [1,2,3,4,5,6]
max1=a[0]
second=a[0]
for i in a:
    if i >max1:
        second=max1
        max1 = i
    elif i > second:
        second =i
print(max1,second)


a = [1, 2, 3, 4, 5, 6]
max_val = 0
second_val = 0

for i in a:
    if i > max_val:
        second_val = max_val
        max_val = i
    elif i > second_val:
        second_val = i

print(max_val, second_val)
