t = [1,2,3,4,5,6,7,8,4,5,6,3,1]
r = {}
for i in t:
    if i in t:
        r[i] +=1
    else:
        r [i]= 1