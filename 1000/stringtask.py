a = input()

up = ["A", "O", "Y", "E", "U", "I"]
down = ["a", "o", "y", "e", "u", "i"]

for n in range(0,6):
  a = (a.translate({ord(up[n]): None}))
  a = (a.translate({ord(down[n]): None}))

a1 = []
for i in range(0,len(a)):
  a1.append(a[i])

m=0                                                           #https://codeforces.com/problemset/problem/118/A
for i in range(0,len(a1)):
  a1.insert(m,'.')
  m+=2

a1 = ''.join(a1)
a1 = a1.lower()
print(a1)
