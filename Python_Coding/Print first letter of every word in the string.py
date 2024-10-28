S = "geeks for geeks"
s= S.strip().lower().split()
a = []
for i in s:
    a.append(i[0])
print(''.join(a))


str = 'i.like.this.program.very.much'
st = str.strip()
stack = []
for i in str:
    stack.append(i)
a = []
while stack:
    for i in stack:
        a.append(i)

print(a)

for i in range(len(st)-1 ,-1, -1):
    print(i)