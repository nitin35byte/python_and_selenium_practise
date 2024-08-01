l = [1,2,3,2,5,6,1,4,5,7]
l = "Ny Name is nitin"
seen = []
duplicate = []

for i in l:
    if i in seen:
        duplicate.append(i)
    else:
        seen.append(i)

print("".join(f"duplicate sgtring is {duplicate} and unique charasters are {seen}"))

class parent():

    def __init__(self,name , age):
        self.name = name
        self.age=age

    def habits(self):
        print("pass")

class monther():
    def __init__(self,name):
        self.name=name
    def habits(self):
        pass