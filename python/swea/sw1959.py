def o():
    return list(map(int,input().split()))
for i in range(int(input())):
    n,m=o()
    a=o()
    b=o()
    r=[]
    if n>m:
        n,m=m,n
        a,b=b,a
    for j in range(m-n+1):
        s=[]
        for k in range(n):
            s.append(a[k]*b[j+k])
        r.append(sum(s))
    print(f'#{i+1} {max(r)}')