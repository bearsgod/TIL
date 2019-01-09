def p(x):
    if x==1:
        return [[1]]
    elif x==2:
        return [[1],[1,1]]
    else:
        l=[]
        k=p(x-1)
        m=k[x-2]
        for i in range(x):
            if i==0 or i==x-1:
                l.append(1)
            else:
                l.append(m[i-1]+m[i])
        k.append(l)
        return k
for i in range(int(input())):
    n=p(int(input()))
    print(f'#{i+1}')
    for j in n:
        for k in j:
            print(k,end=' ')
        print()