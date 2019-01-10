for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    d=[]
    for j in range(n-1):
        d.append(l[j]-l[j+1])
    u=min(d)
    a=max(d)
    if u>0:
        u=0
    if a<0:
        a=0
    print(f'#{i+1} {abs(u)} {a}')