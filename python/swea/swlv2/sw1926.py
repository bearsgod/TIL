for i in range(1,int(input())+1):
    s=str(i)
    b=s.count('3')+s.count('6')+s.count('9')
    if b>0:
        s='-'*b
    print(s,end=' ')