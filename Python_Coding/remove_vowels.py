S = "welcome to geeksforgeeks"
vowels = 'aeiou'
s = S.strip().lower()
without_vowels=[]
for i in s:
    if i in vowels:
        continue
    without_vowels.append(i)

print(''.join(without_vowels))


#List Comprehnsion
without_vowel = [i for i in s if i not in vowels]

print(''.join(without_vowel))