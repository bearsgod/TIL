# sw 1983
s = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
def z(n,m,o):
    return n*0.35+m*0.45+o*0.2
for i in range(int(input())):
    t = input().split()
    l = {}
    for j in range(int(t[0])):
        a,b,c = tuple(map(int,input().split()))
        l[j] = z(a,b,c)
    k = sorted(l.values())
    p = k.index(l[int(t[1])-1])
    print(f'#{i+1} {s[10-int((((p+1)/int(t[0]))*10))]}')