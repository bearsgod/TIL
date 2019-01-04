n = int(input())
endn = 1
r = 1
while endn < n:
    r += 1
    endn += r
l = []
for i in range(r):
    l.append((r-i,i+1))
k = n - endn + r
if r % 2:
    a,b = l[k-1]
else:
    a,b = l[r-k]
print(f'{a}/{b}')

for i in range(int(input()),0):
    print(i,end=' ')