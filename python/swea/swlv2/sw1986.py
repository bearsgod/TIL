for i in range(int(input())):
    s=0
    for j in range(1,int(input())+1):
        if j%2:
            s+=j
        else:
            s-=j
    print(f'#{i+1} {s}')