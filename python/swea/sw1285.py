for i in range(int(input())):
    h = int(input())
    c = list(map(abs,map(int,input().split())))
    f = 100001
    n = 0
    for j in c:
        if j < f:
            n = 1
            f = j
        elif j == f:
            n += 1
    print(f'#{i+1} {f} {n}')