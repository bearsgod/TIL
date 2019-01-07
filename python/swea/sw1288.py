for i in range(int(input())):
    n = int(input())
    j = 0
    t = 0
    p = ()
    while t == 0:
        j+=1
        c = n * j
        p += tuple(str(c)[::1])
        for k in range(10):
            if not str(k) in p:
                break
        else:
            t = 1
    print(f'#{i+1} {j}')