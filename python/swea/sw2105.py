for t in range(int(input())):
    lines=[]
    for n in range(int(input())):
        lines.append(list(map(int,input().split())))
    base=n+1
    maxnum=-1
    goleft=goright=0
    for i in range(base-2):
        for j in range(1,base-1):
            limit=n-i
            if j>=limit:
                leftmax=limit-1
            else:
                leftmax=j
            dessertlist=[]
            cursor=lines[i][j]
            dessertlist.append(cursor)
            for ld in range(leftmax,0,-1):
                dessertlist=dessertlist[:1]
                for a in range(1,ld+1):
                    cursor=lines[i+a][j-a]
                    dessertlist.append(cursor)
                goleft=a
                for rd in range(limit-ld,0,-1):
                    try:
                        for b in range(1,rd+1):
                            cursor=lines[i+a+b][j-a+b]
                            dessertlist.append(cursor)
                        goright=b
                        for c in range(1,a+1):
                            cursor=lines[i+a+b-c][j-a+b+c]
                            dessertlist.append(cursor)
                        for d in range(1,b+1):
                            if i+a+b-c-d==i:
                                break
                            cursor=lines[i+a+b-c-d][j-a+b+c-d]
                            dessertlist.append(cursor)
                    except IndexError:
                        dessertlist=dessertlist[:goleft+1]
                        continue
                    token=1
                    for e in dessertlist:
                        if dessertlist.count(e)>1:
                            token=0
                            break
                    if token:
                        temp=len(dessertlist)
                        if maxnum<temp:
                            maxnum=temp
                    print(dessertlist)
                    dessertlist=dessertlist[:goleft+1]
    print(f'#{t+1} {maxnum}')