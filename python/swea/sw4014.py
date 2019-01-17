def spliting(ls):
    splits=[]
    s=len(ls)
    while ls:
        sp=[]
        token=0
        for i in range(len(ls)):
            if i==0:
                sp.append(ls[i])
            else:
                if ls[i]==sp[0]:
                    sp.append(ls[i])
                else:
                    token=1
            if token:
                break
        splits.append(sp)
        splitslen=0
        for j in range(len(splits)):
            splitslen+=len(splits[j])
        if splitslen==s:
            break
        ls=ls[i:]
    return splits

def check(ls):
    global x
    s=len(ls)
    numl=[]
    for i in range(s):
        numl.append(ls[i][0])
    if s==1:
        return True
    for i in range(s-1):
        if abs(numl[i]-numl[i+1])>1:
            return False
        try:
            if numl[i]>numl[i+1]:
                if len(ls[i+1])<x:
                    return False
                else:
                    for j in range(x):
                        ls[i+1].remove(ls[i+1][0])
            else:
                if len(ls[i])<x:
                    return False
                else:
                    for k in range(x):
                        ls[i].remove(ls[i][0])
        except IndexError:
            return False
    return True

for t in range(int(input())):
    n,x=list(map(int,input().split()))
    heights_row=[]
    heights_column=[]
    for i in range(n):
        heights_row.append(list(map(int,input().split())))
    for j in range(n):
        column=[]
        for k in range(n):
            column.append(heights_row[k][j])
        heights_column.append(column)
    counter=0
    for m in range(n):
        if check(spliting(heights_column[m])):
            counter+=1
        if check(spliting(heights_row[m])):
            counter+=1
    print(f'{t+1} {counter}')