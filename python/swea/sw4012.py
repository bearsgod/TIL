for i in range(int(input())):
    n=int(input())
    a=[list(map(int,input().split())) for i in range(n)] # 원래 행렬
    # 절반 쪼개기
    uphalf=[]
    downhalf=[]
    for i in range(n):
        for j in range(i,n):
            uphalf.append(a[i][j])
            downhalf.append(a[j][i])
    # 요리 하나하나 나올 수 있는 점수 다 가져옴
    casenum=n/2-1
    num=n*(n-1)/2
    