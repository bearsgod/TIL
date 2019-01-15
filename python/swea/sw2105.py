for t in range(int(input())):
    lines=[]
    for n in range(int(input())):
        lines.append(list(map(int,input().split())))
    minnum=0
    for i in range(n-2):
        for j in range(1,n-1):
            leftmax=j
            rightmax=n-1-j
            dessertlist=[]
            cursor=lines[i][j]
            dessertlist.append(cursor)
            for ld in range(leftmax,0,-1):
                for a in range(1,ld+1):
                    cursor=lines[i+a][j-a]
                    dessertlist.append(cursor)
                for rd in range(rightmax,0,-1):
