s = input()
ch = ['c=','c-','d-','lj','nj','s=','z=']
ch2 = 'dz='
l = len(s)
for i in range(len(s)-1):
    for j in ch:
        if j == s[i:i+2]:
            l -= 1
for i in range(len(s)-2):
    if ch2 == s[i:i+3]:
        l -= 1
print(l)