for i in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    c = []
    for j in range(101):
        c.append(l.count(j))
    t = 0
    for k in range(len(c)):
        if c[k] == max(c):
            t = k
    print(f'#{n} {t}')