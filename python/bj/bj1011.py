tcn = int(input())
    
for i in range(tcn):
    tc = input()
    s,f = tc.split(' ')
    dt = int(f) - int(s)
    n = 1
    maxdt = 1
    while dt > maxdt:
        if n % 2:
            maxdt = ((n+1)/2)**2
        else:
            maxdt = (n/2+1)**2 - (n/2+1)
        n += 1
    if dt == 1:
        print(n)
    else:
        print(n-1)