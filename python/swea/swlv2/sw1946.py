for i in range(int(input())):
    s=''
    for j in range(int(input())):
        a,b=input().split()
        s+=a*int(b)
        t=len(s)//10
    l=[s[n*10:n*10+10] for n in range(len(s)//10)]+[s[t*10:]]
    print(f'#{i+1}')
    [print(k) for k in l]