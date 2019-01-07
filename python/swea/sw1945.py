for i in range(int(input())):
    n = int(input())
    l=[11,7,5,3,2]
    f=[]
    for j in l:
        k=0
        while n%j==0:
            n//=j
            k+=1
        f.insert(0,k)
    print(f'#{i+1}',f[0],f[1],f[2],f[3],f[4])