for i in range(int(input())):
    s=input().strip()
    t=0
    if s==s[::-1]:
        t=1
    print(f'#{i+1} {t}')