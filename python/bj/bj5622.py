s = input()
l = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
sumsec = 0
for i in s:
    for j in range(len(l)):
        if i in l[j]:
            sumsec += j + 3
print(sumsec)