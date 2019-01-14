def clearing(ls,x,y):
    value=ls[x][y]
    if value==1:
        checkboard[x][y]=0
    elif value>1:
        if value-2>y:
            for i in range()

def search(idx,ls):
    global n,w,h,minnum
    if idx==n:
        summary=0
        for i in range(h):
            summary+=ls[i].count(0)
        if minnum>summary:
            minnum=summary
    else:
        if trial[0]>0:
            v=trial-1
            trial[0]-=1
            
            
for t in range(int(input())):
    n,w,h=list(map(int,input().split()))
    gameboard=[]
    for row in range(h):
        gameboard.append(list(map(int,input().split())))
    checkboard=[[1 for width in range(w)] for height in range(h)]
    minnum=180
    trial=[w for tring in range(n)]