s=['D0', 'C-', 'C0', 'C+', 'B-', 'B0', 'B+', 'A-', 'A0', 'A+']
for i in range(int(input())):
    t=input().split()
    l={}
    for j in range(int(t[0])):
        a,b,c=list(map(int,input().split()))
        l[j]=a*0.35+b*0.45+c*0.2
    k=sorted(l.values())
    p=k.index(l[int(t[1])-1])
    print(f'#{i+1} {s[int((((p)/int(t[0]))*10))]}')