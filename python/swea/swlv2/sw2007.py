for i in range(int(input())):
    s=input()
    for j in range(1,11):
        if s[0:j]==s[j:2*(j)]:
            break
    print(f'#{i+1} {j}')