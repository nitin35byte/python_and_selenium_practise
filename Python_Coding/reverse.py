string = "My Name Is NItin"
# left = 0
# right = len(string)-1
# while left <right:
#     string[left],string[right]=string[right],string[left]
#     left +=1
#     right-=1
#
# print(string)

string = "My Name Is NItin"
words = string.split()  # Split the string into words

for i in words:
    word = i[0].upper() + i[1:].lower()
    print("".join(word))
