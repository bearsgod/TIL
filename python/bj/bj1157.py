k = input()
l = {}
s = []
t = 0
for i in range(65,91):
    n = k.count(chr(i))+k.count(chr(i+32))
    if n == 0:
        continue
    elif n in l.keys():
        t = 1
        s.append(n)
    else:
        l[n] = chr(i)
if t and max(l.keys()) in s:
    print('?')
else:
    print(l[max(l.keys())])