for i in range(int(input())):
    n,r=list(map(int,input().split()))
    c1=list(range(n,n-r,-1))
    c2=list(range(r,0,-1))
    c11=1
    c22=1
    for j in c1:
        c11*=j
    for k in c2:
        c22*=k
    c=c11//c22
    print(c%1234567891)