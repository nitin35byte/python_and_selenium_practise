l = [0,3,1]
N = len(l)
arr_sum= N * (N+1)//2
total_sum= sum(l)

diff = arr_sum-total_sum
print(diff)


lst= "My name is nitin"
lst= lst.strip().split()
stack = []
for i in lst:
    stack.append(i)
word = []
while stack:
    word.append(stack.pop())

print(" ".join(word))

seen = set()
duplicate= []
for i in lst:
    if i not in seen:
        seen =i
    else:
        duplicate +=1
print(f"dulicate values are:",duplicate)