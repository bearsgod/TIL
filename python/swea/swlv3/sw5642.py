for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    m,s=0,0
    for j in l:
        s+=j
        if s>m:
            m=s
        if s<0:
            s=0
    print(f'#{i+1} {m}')