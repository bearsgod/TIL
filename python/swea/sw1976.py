for i in range(int(input())):
    w,x,y,z=list(map(int,input().split()))
    a=x+z
    b=w+y
    if a>59:
        a-=60
        b+=1
    if b>12:
        b-=12
    print(f'#{i+1} {b} {a}')        