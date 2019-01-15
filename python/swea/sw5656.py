def clearing(ls,x,y):
    global gameboard
    value=ls[x][y]
    if value==1:
        gameboard[x][y]=0
        checkboard[x][y]=1
    elif value>1:
        if value-2<y:
            for i in range(y):
                gameboard[x][i]=0
                checkboard[x][i]=1
        else:
            for i in  range(y-value-2,y):
                gameboard[x][i]=0
                checkboard[x][i]=1
        if value+y-1>w:
            for i in range(y+1,w):
                gameboard[x][i]=0
                checkboard[x][i]=1
        else:
            for i in range(y+1,y+value):
                gameboard[x][i]=0
                checkboard[x][i]=1
        if value+x-1>h:
            for i in range(x+1,h):
                gameboard[i][y]=0
                checkboard[i][y]=1
        else:
            for i in range(x+1,x+value):
                gameboard[i][y]=0
                checkboard[i][y]=0
        gameboard[x][y]=0
    for k in range(w):
        for j in range(h-1,-1,-1):
            if gameboard[j][k]==0:
                for m in range(j):
                    gameboard[m][k]=0
                    checkboard[m][k]=1
            break

def search(idx,ls):
    global n,w,h,minnum
    if idx==n:
        summary=0
        for i in range(h):
            summary+=ls[i].count(0)
        if minnum>summary:
            minnum=summary
    else:
        for j in range(w):
            if trial[j]>0:
                temp=ls[:][:]
                trial[j]-=1
                for i in range(h):
                    if gameboard[i][j]:
                        x=i
                        clearing(ls,x,j)
                        search(idx-1,ls)
                gameboard=temp
            
            
            
for t in range(int(input())):
    n,w,h=list(map(int,input().split()))
    gameboard=[]
    for row in range(h):
        gameboard.append(list(map(int,input().split())))
    checkboard=[[0 for width in range(w)] for height in range(h)]
    minnum=180
    trial=[n for tring in range(w)]
    temp=[]