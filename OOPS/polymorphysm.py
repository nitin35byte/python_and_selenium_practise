class MyClass:
    def instance_method(self):
        return "Instance method called"

    def another_method(self):
        # Calling the instance method from another method
        return self.instance_method()

# Create an instance of the class
obj = MyClass()
print(obj.another_method())  # Output: Instance method called


class shape:
    """
            1. This is method overloading example
            2. Method Overloading is used make code readable and cleaner
            3. Python does not support Polymorphism (method overloading)  , but python does not support  method overloading python provide different method to achiev this
            4. Three type of polymorphism
            4.1. Method Overriding
            4.2. Method overloading
            4.3. Operator Overloading

    """
    def area(self , radius):
        return 4.13 * radius * radius

    def area(self , l,b):
        return l *b

s=shape()
s.area(2)
s.area(3,5)


## In This way we can achieve method overloading
class shape():

    def area(self , a, b=0):
        if b==0:
            return 3.14 * a * a
        else:
            return a *b

s1= shape()
print(s1.area(2))
print(s1.area(3,5))


### operator overloading
print("hellow" + ' ' +"world")

print( 6 +9)

print([2,3,4,5] +[4,5])




## Method Overriding
# Superclass or Parent Class
class Phone:
    def __init__(self, model, name):
        self.name = name
        self.model = model

    def buy(self):
        return "Buying a phone from the parent class"

# Subclass or Child Class
class Product(Phone):
    # Method overriding
    def buy(self):
        return "Buying a product from the subclass"

# Create object of subclass
product = Product("iPhone", "Apple")

# Call the overridden method
print(product.buy())  # Output: Buying a product from the subclass
