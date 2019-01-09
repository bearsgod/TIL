for i in range(int(input())):
    l=list(map(int,input().split()))
    print(f'#{i+1} {int(round((sum(l)-max(l)-min(l))/8))}')