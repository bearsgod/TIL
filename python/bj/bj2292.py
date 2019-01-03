n = int(input())
endn = 1
i = 0
while endn < n:
    endn += 6 * (i+1)
    i += 1
print(i+1)