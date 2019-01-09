for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=0
    t=0
    while t<n-1:
        m=max(l[t:])
        d=l[t:].index(m)
        if not d:
            t+=1
        else:
            for j in range(t,d+t):
                s+=m-l[j]
            t=d+t+1
    print(f'#{i+1} {s}')