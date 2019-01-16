'''
1: 상하좌우
2: 상하
3: 좌우
4: 상우(ㄴ)
5: 하우(r)
6: 하좌(ㄱ)
7: 상좌(j)
'''
def cango(ls,x,y):
    shape=ls[x][y]
    if shape==1:
        position=[[x,y+1],[x,y-1],[x+1,y],[x-1,y]]
    elif shape==2:
        position=[[x+1,y],[x-1,y]]
    elif shape==3:
        position=[[x,y+1],[x,y-1]]
    elif shape==4:
        position=[[x-1,y],[x,y+1]]
    elif shape==5:
        position=[[x+1,y],[x,y+1]]
    elif shape==6:
        position=[[x+1,y],[x,y-1]]
    elif shape==7:
        position=[[x-1,y],[x,y-1]]
    return position
def checkline(ls,x1,y1,x2,y2):
    position=cango(ls,x2,y2)
    if [x1,y1] in position:
        return True
def bfs(idx,ls,x,y):
    global n,m,l,r,c
    check[x][y]=1
    if idx<l:
        position=cango(ls,x,y)
        for item in position:
            new_x=item[0]
            new_y=item[1]
            if new_x<n and new_y<m and new_x>=0 and new_y>=0:
                if ls[new_x][new_y] and checkline(ls,x,y,new_x,new_y):
                    item2 = ls[x][y]
                    ls[x][y] = 0
                    bfs(idx+1,ls,new_x,new_y)
                    ls[x][y] = item2

for t in range(int(input())):
    n,m,r,c,l=list(map(int,input().split()))
    maps=[]
    for line in range(n):
        maps.append(list(map(int,input().split())))
    check=[[0 for x in range(m)] for x in range(n)]
    bfs(1,maps,r,c)
    where=0
    for i in range(n):
        where+=check[i].count(1)
    print(f'#{t+1} {where}')