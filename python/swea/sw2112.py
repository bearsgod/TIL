def search(ls,idx):
    global d,w,k,trying
    if idx==k:
        return k
    passing=0
    for j in range(w):
        for i in range(d-k+1):
            a=ls[i][j]
            for l in range(1,k):
                if ls[i+l][j]!=a:
                    break
            else:
                passing+=1
                break
    if passing==w and idx==0:
        return 0
    else:
        


d,w,k=list(map(int,input().split()))
films=[]
for page in range(d):
    films.append(list(map(int,input().split())))
trying=0
search(films,0)
print(trying)