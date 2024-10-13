p = {}
target = 'i'
stringt = "Your sample text here including some I's"  # Replace with your string

for i in stringt.lower():
    if i == target:
        p[i] = p.get(i, 0) + 1


for i in stringt.lower():
    if i =='o':
        if i in p:
            p[i]+=1
        else:
            p[i]=1

print(p)


string = "Your sample text here including some I's"
count = string.lower().count('i')

print(f"coount of {count}  is ",count)
