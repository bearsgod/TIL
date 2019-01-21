for T in range(int(input())):
    n,m,k=list(map(int,input().split()))
    case=[]
    for column in range(n):
        row=list(map(int,input().split()))
        case_row=[]
        for row2 in range(m):
            case_row.append([row[row2],0])
    for time in range(k):
        
        for column in range(n):
            for row in range(m):
                target=case[n][m]
                if time-target[1]==target[0]+1:
                    