num= int(input("enter number"))

if num ==0:
    print("please enter valid number")
elif num ==1:
    print("factorial of 1 is one")
else:
    product = 1
    for i in range(1, num +1):
        product = product*i
    print(product)

