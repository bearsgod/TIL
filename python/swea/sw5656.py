import copy,itertools
def clear(ls,x,y):
    global w,h
    num=ls[x][y]
    if num==1:
        ls[x][y]=0
    elif num>1:
        for left in range(num-1):
            if x-left<0:
                break
            else:
                clear(ls,x-left,y)
        for right in range(1,num):
            if x+right>w-1:
                break
            else:
                clear(ls,x+right,y)
        for down in range(1,num):
            if y+down>h-1:
                break
            else:
                clear(ls,x,y+down)
        ls[x][y]=0
for t in range(int(input())):
    n,w,h=list(map(int,input().split()))
    gamerow=[]
    for line in range(h):
        rows=list(map(int,input().split()))
        gamerow.append(rows)
    gamepan=[]
    for i in range(w):
        gamecolumn=[]
        for j in range(h):
            gamecolumn.append(gamerow[j][i])
        gamepan.append(gamecolumn)
    where_to_shot=itertools.product([x for x in range(w)],repeat=n)
    minnum=w*h
    for pro in where_to_shot:
        a=copy.deepcopy(gamepan)
        counter=0
        for shot in pro:
            for high in range(h):
                if a[shot][high]:
                    clear(a,shot,high)
                    break
            for row2 in range(w):
                for m in range(h-1,-1,-1):
                    if not a[row2][m]:
                        index=m
                        break
                for delete in range(h-m-1):
                    a[row2][delete]=0
        for weight in range(w):
            for height in range(h):
                if a[weight][height]:
                    counter+=1
        if minnum>counter:
            minnum=counter
    print(f'#{t+1} {minnum}')