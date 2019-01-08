for i in range(int(input())):
    r=[]
    s=[]
    for j in range(9):
        r.append(list(map(int,input().split())))
    for k in range(3):
        a=3*k
        for l in range(3):
            b=3*l
            t=[]
            for m in range(3):
                for n in range(3):
                    t.append(r[a+m][b+n])
            s.append(t)
    c=[]
    for x in range(9):
        t=[]
        for y in range(9):
            t.append(r[y][x])
        c.append(t)
    h=[r,s,c]
    p=1
    for z in range(1,10):
        for q in h:
            for u in range(9):
                if q[u].count(z) > 1:
                    p=0
    print(f'#{i+1} {p}')