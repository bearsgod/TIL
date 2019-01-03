tcn = int(input())
for i in range(tcn):
    tc = input()
    s,f = tc.split(' ')
    dt = int(f) - int(s)
    maxtry = 0
    k = 0
    while maxtry < dt:
        k += 1
        j = k//2 + 1
        if k % 2:
            maxtry = j + sum(range(j)) * 2
        else:
            maxtry = sum(range(j)) * 2
    print(k)