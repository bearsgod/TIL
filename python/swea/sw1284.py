for i in range(int(input())):
    p,q,r,s,w = tuple(map(int,input().split()))
    a = p * w
    if w <= r:
        b = q
    else:
        b = q + s * (w-r)
    if a > b:
        d = b
    else:
        d = a
    print(f'#{i+1} {d}')    