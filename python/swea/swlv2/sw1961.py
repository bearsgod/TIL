for i in range(int(input())):
    n=int(input())
    a=[list(input().split()) for m in range(n)]
    r=['' for i in range(n)]
    for c in range(3):
        p=['' for i in range(n)]
        for k in range(n):
            for j in range(n):
                p[k] += a[n-j-1][k]
        a=p
        for l in range(n):
            r[l] += p[l] + ' '
    print(f'#{i+1}')
    [print(r[w]) for w in range(n)]