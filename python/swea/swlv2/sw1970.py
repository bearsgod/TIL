for i in range(int(input())):
    n=int(input())
    f=[50000,10000,5000,1000,500,100,50,10]
    a=[]
    for j in f:
        a.append(n//j)
        n%=j
    print(f"#{i+1}\n{' '.join(list(map(str,a)))}")