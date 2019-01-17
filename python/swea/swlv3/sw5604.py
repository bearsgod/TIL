def rangesum(x):
    for big in range(17):
        if x<10**big:
            break
    if not big:
        return 0
    first_x = x//(10**(big-1))
    if big==1:
        return sum(range(first_x+1))
    else:
        temp=(first_x*(big-1)*(10**(big-2))*45)+(sum(range(first_x))*(10**(big-1)))+first_x
        temp2=0
        temp3=0
        if (x-first_x*10**(big-1)):
            temp2=(x-first_x*10**((big-1)))*first_x
            temp3=rangesum(x-first_x*10**(big-1))
        return temp+temp2+temp3

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