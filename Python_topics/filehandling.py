f = open("test.txt" , 'w')
f.write("my name is nitin \n i am earning file handling")
f.close()

f= open("test.txt" , 'a')
f.write("\ntodays date is 14-9-2024")
f.close()


## add mutilpe line in single line
l =[ "i m from ddelhi\n" "My dreas is to go to abrod\n","i joined rk fitnes",]
f = open('test1.txt' ,'w')
f.writelines(l)
f.close()

##Cound character and display
f = open('test1.txt' ,'r')
s=f.read(10)
print(s)
f.close()


f=open('test.txt' ,'r')
s = f.read()
print(s)
f.close()


# f= open('test1.txt' ,'r')
# print(f.readline() , end="##")
# print(f.readline() , end="##")

# f= open('test1.txt' ,'r')
# while True:
#     data= f.readline()
#     if data == ' ':
#         break
#     else:
#         print(data , end='')
#
# f.close()

with open("test2.txt" ,'w') as f:
    f.write("hello world")


# with open('test2.txt' ,'r') as f:
    #print(f.readline())



with open("test2.txt" ,'r') as f:
    chunk_size=10

    while len(f.read(chunk_size)) >0:
        print(f.read(chunk_size) , end = "***")
        f.read(chunk_size)
