def search(ls,idx,link):
    global pro,linked,length,temp,linked
    nlink=link
    linklen=0
    if idx==len(ls):
        if linked<link:
            length=temp
            linked=link
        elif linked==link:
            if temp<length:
                print()
                for i in range(n):
                    for j in range(n):
                        print(pro[i][j],end=' ')
                    print()
                length=temp
    else:
        c=ls[idx]
        # 상
        tag=[]
        for i in range(c[0]-1,-1,-1):
            if pro[i][c[1]]:
                linklen=0
                break
            else:
                linklen+=1
                pro[i][c[1]]=2
                tag.append([i,c[1]])
        if linklen!=0:
            link+=1
            temp+=linklen
        search(ls,idx+1,link)
        temp-=linklen
        link=nlink
        linklen=0
        for i in tag:
            pro[i[0]][i[1]]=0
        # 하
        tag=[]
        for i in range(c[0]+1,n):
            if pro[i][c[1]]:
                linklen=0
                break
            else:
                linklen+=1
                pro[i][c[1]]=2
                tag.append([i,c[1]])
        if linklen!=0:
            link+=1
            temp+=linklen
        search(ls,idx+1,link)
        temp-=linklen
        link=nlink
        linklen=0
        for i in tag:
            pro[i[0]][i[1]]=0
        # 좌
        tag=[]
        for i in range(c[1]-1,-1,-1):
            if pro[c[0]][i]:
                linklen=0
                break
            else:
                linklen+=1
                pro[c[0]][i]=2
                tag.append([c[0],i])
        if linklen!=0:
            link+=1
            temp+=linklen
        search(ls,idx+1,link)
        temp-=linklen
        link=nlink
        linklen=0
        for i in tag:
            pro[i[0]][i[1]]=0
        # 우
        tag=[]
        for i in range(c[1]+1,n):
            if pro[c[0]][i]:
                linklen=0
                break
            else:
                linklen+=1
                pro[c[0]][i]=2
                tag.append([c[0],i])
        if linklen!=0:
            link+=1
            temp+=linklen
        search(ls,idx+1,link)
        temp-=linklen
        link=nlink
        linklen=0
        for i in tag:
            pro[i[0]][i[1]]=0
        # 안함
        search(ls,idx+1,link)
for T in range(int(input())):
    n=int(input())
    pro=[]
    check_core=[]
    for i in range(n):
        pro.append(list(map(int,input().split())))
    for i in range(n):
        for j in range(n):
            if 0<i<n-1 and 0<j<n-1:
                if pro[i][j]:
                    if pro[i-1][j] and pro[i+1][j] and pro[i][j-1] and pro[i][j+1]:
                        continue
                    else:
                        check_core.append([i,j])
    link=0
    linked=0
    temp=0
    length=n*n
    search(check_core,0,0)
    print(f'#{T+1} {length}')