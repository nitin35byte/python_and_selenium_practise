t = [1,2,3,4,5,6,7,8,4,5,6,3,1]
r = {}
for i in t:
    if i in t:
        t[i] +=1
    else:
        t[i]= 1
print(t)
t[0]="Apple"
print(t)
t.extend([1,2,3,4,5])
print(t)

a = (1,2 ,3,[2,3,4,5],3,4,[4,6])
print(type(a))
print(a)
a[3][0]=4
print(a)

#a[3]=[1,2,44,5]
# print(a)

c = {1,2,3,4,5,6,'apple'}
print(type(c))

print(c)

# def total_sum(l):
#     total =0
#     for i in l:
#         if isinstance(i , list):
#         #if type(i) ==list:
#             total+=total_sum(i)
#         else:
#             total +=i
# x = (1,2 ,3,[2,3,4,5],3,4,[4,6])
# obj = total_sum(x)
# print(obj)
#
# def total_sum(l):
#     total = 0
#     for i in l:
#         # Check if the element is a list
#         if isinstance(i, list):
#             total += total_sum(i)  # Recursive call for sublist
#         else:
#             total += i  # Add the element to the total
#     return total  # Return the accumulated total
#
# # Example list with nested lists
# x = [1, 2, [3, 4], [5, [6, 7]]]
#
# # Call the function and print the result
# obj = total_sum(x)
# print(obj)  # Output: 28

c = [1,2,3,4,5,6,'apple']
for i in range(len(c)-1,-1,-1):
    print(c[i])
def reverse_list(c):
    left = 0
    right = len(c) -1
    while left < right:
        c[left] , c[right] = c[right], c[left]
        left +=1
        right -=1
    return c
obj=reverse_list(c)
print(f"below are the reverr list:",obj)


# lower = int(input("enter lower number"))
# upper = int(input("enter upper number"))
#
# for i in range(2 , lower +1):
#     for j in range(1 , i+1):
#         if i %j ==0:
#             break
#         print(i)


class  test:
    def car(self):
        print('pass')
t = test()
t.car()
