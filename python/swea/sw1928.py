b=[chr(k) for k in range(65,91)]+[chr(k) for k in range(97,123)]+[str(k) for k in range(10)]+['+','/']
for i in range(int(input())):
    n=input()
    l=[n[t*4:t*4+4] for t in range(len(n)//4)]
    print(f'#{i+1} ',end='')
    for j in l:
        c=''
        for k in range(4):
            c+=str(bin(b.index(j[k]))[2:].zfill(6))
        for m in range(3):
            a=chr(int(c[m*8:m*8+8],2))
            print(a,end='')
    print()