def search(ls,x,y,dig):
    global n,k
    high=ls[x][y]
    if x>0:
        if high>ls[x-1][y]:
            search(ls,x-1,y,dig)
        elif dig==0 and ls[x-1][y]-high<k:
            dig=1
            for k in range(1,k+1):
                temp,ls[x-1][y]=ls[x-1][y],ls[x-1][y]-k
                search(ls,x-1,y,dig)
                ls[x-1][y]=temp
            dig=0
    if x<n:
        if high>ls[x+1][y]:
            search(ls,x+1,y,dig)
        elif dig==0 and ls[x+1][y]-high<k:
            dig=1
            for k in range(1,k+1):
                temp,ls[x+1][y]=ls[x+1][y],ls[x+1][y]-k
                search(ls,x+1,y,dig)
                ls[x+1][y]=temp
            dig=0
    if y>0:
        if high>ls[x][y-1]:
            search(ls,x,y-1,dig)
        elif dig==0 and ls[x][y-1]-high<k:
            dig=1
            for k in range(1,k+1):
                temp,ls[x][y-1]=ls[x][y-1],ls[x][y-1]-k
                search(ls,x,y-1,dig)
                ls[x][y-1]=temp
            dig=0
    if y<n:
        if high>ls[x][y+1]:
            search(ls,x,y+1,dig)
        elif dig==0 and ls[x][y+1]-high<k:
            dig=1
            for k in range(1,k+1):
                temp,ls[x][y+1]=ls[x][y+1],ls[x][y+1]-k
                search(ls,x,y+1,dig)
                ls[x][y+1]=temp
            dig=0

n,k=list(map(int,input().split()))
maps=[]
maxhigh=0
tips=[]
for i in range(n):
    maps.append(list(map(int,input().split())))
    if maxhigh<max(maps[i]):
        maxhigh=max(maps[i])
for i in range(n):
    for j in range(n):
        if maps[i][j]==maxhigh:
            tips.append([i,j])
longest=0