def rangesum(x):
    for big in range(15):
        if x<10**big:
            break
    if not big:
        big = 1
    first_x = x//(10**(big-1))
    if big == 1:
        return sum(range(first_x))+first_x
    elif big == 2:
        temp = 0
        for j in range(first_x):
            temp += j*10**(big-1)
        middle = first_x*((x%10**(big-1))+1) + temp
        return 45*first_x + middle + rangesum(x%(10**(big-1)))        
    else:
        temp = 0
        for j in range(first_x):
            temp += j*10**(big-1)
        middle = first_x*((x%10**(big-1))+1) + temp
        return 45*first_x*10*(big-1) + middle + rangesum(x%(10**(big-1)))

T = int(input())
for test_case in range(1, T + 1):
    start,end=map(int ,input().split())
    if start:
        sum_start = rangesum(start-1)
    else:
        sum_start = rangesum(start)
    sum_end = rangesum(end)
    my_sum = sum_end - sum_start
    print(f'#{test_case} {my_sum}')