
def nonRepeatingChar(s):
    seen = {}
    non_repe=[]

    for i in s:
        if i in seen:
            seen[i]+=1
        else:
            seen[i] = 1
            non_repe.append(i)
    # return non_repe

    for char in non_repe:
        if seen[char] == 1:
            return char

    return None



s='geeksforgeeks'
a = nonRepeatingChar(s)
print(a)
