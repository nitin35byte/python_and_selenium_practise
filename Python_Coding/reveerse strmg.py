l = 'abcdefg'
b = l[::-1]
print(b)


def is_palindrome(lst):
    word = ''.join(lst.split())  # Join the list of words into a single string

    left = 0
    right = len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False

        left += 1
        right -= 1
    return True

string = "My Name Is NItin"
if is_palindrome(string):
    print("Palindrome")
else:
    print("Not Palindrome")


k= 2
l =[1,2,9,0,0,5,5,2]
count = []
num = []
for i in l:
    count.append(i)

    if count.count(i)==k and i not in num:
        num.append(i)
print(num)
