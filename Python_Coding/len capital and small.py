word = "My name Is niTiN aNd I hAve inervzxncssdasSDSDSDSD"
lower = 0
capital=0
word_1=[]
word_2=[]

for i in word:
    if  65<= ord(i)<= 90:
        capital +=1
        word_1.append(i)
    elif 97<= ord(i)<= 122:
        lower +=1
        word_2.append(i)


print("lower:",lower)
print("cap:",capital)
print("word_1:",word_1)
print("word_2:",word_2)


l = [1,2,3,4,5,6,7,8,9]
w=[x for x in l if x%2!=0]
print(w)


total =0
for i in range(len(l)):
    total +=l[i]
print(total)