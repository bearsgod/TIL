def operset(iter):
    n=len(iter)
    indices=list(range(n))
    cycles=list(range(n,0,-1))
    

import itertools

for i in range(int(input())):
    n=int(input())
    o=list(map(int,input().split()))
    numl=list(map(int,input().split()))
    operators=['+','-','*','/']
    operl=[0 for num in range(n-1)]
    firstindex=0
    for j in range(4):
        token=0
        for k in range(o[j]):
            operl[firstindex+k]=operators[j]
            token+=1
        firstindex+=token
    minnum=1000000000
    maxnum=-1000000000
    for x in set(itertools.permutations(operl)):
        result=numl[0]
        for y in range(len(x)):
            if x[y]=='+':
                result+=numl[y+1]
            elif x[y]=='-':
                result-=numl[y+1]
            elif x[y]=='*':
                result*=numl[y+1]
            else:
                result=int(result/numl[y+1])
        if result<minnum:
            minnum=result
        if result>maxnum:
            maxnum=result
    answer=maxnum-minnum
    print(f'#{i+1} {answer}')