for i in range(int(input())):
    n = r = int(input())
    c = n - r
    a = [[0 for i in range(n)] for j in range(n)]
    num = 1
    breakt = 0
    while r != 0:
            for w in range(c,r):
                a[n-r][w] = num
                num += 1
                if num == n*2:
                    r = 0
                    breakt = 1
                    break
            if breakt:
                break
            for x in range(c+1,r):
                a[x][w] = num
                num += 1
            for y in range(r-2,c-1,-1):
                a[x][y] = num
                num += 1
                if num == n*2:
                    r = 0
                    breakt = 1
                    break
            if breakt:
                break
            for z in range(r-2,c,-1):
                a[z][n-r] = num
                num += 1
            r -= 1
            c += 1
    print(f'#{i+1}')
    for g in range(n):
        for k in range(n):
            print(a[g][k],end=' ')
        print()