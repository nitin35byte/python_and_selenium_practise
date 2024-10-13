import json
l =[ 0,1 ,2 ,3 ,4]

"""
1. Serialization - process of converting python data types to JSON format
2. Deserialization - process of converting JSON to python data types
"""
with open("json.txt" , 'w') as f:
    json.dump(l , f)


d = {
    "Name": 'Nitin',
    "Age" : '27',
    "Gender": 'Male'
}

with open("dict.txt" ,'w')as f:
    json.dump(d, f , indent=4)

#Serializing and Deserializing custom objects
class Person:

    def __init__(self, fname , lname , age , gender):
        self.fname=fname
        self.lname=lname
        self.age= age
        self.gender= gender

person=Person("Nitin" , 'Chaudhary' ,'age' , "Male")
print(person)


def show_object(person):
    if isinstance(person, Person):
        return "{} {}  age ->{}  gender ->{}".format(person.fname , person.lname , person.age , person.gender)
with open('demo.json','w') as f:
  json.dump(person,f,default=show_object)

with open('demo.json','r') as f:
  d = json.load(f)
  print(d)
  print(type(d))