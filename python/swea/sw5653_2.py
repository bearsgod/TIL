for T in range(int(input())):
    n,m,k=list(map(int,input().split()))
    case=[]
    counting=0
    for column in range(n):
        row=list(map(int,input().split()))
        case_row=[]
        for row2 in range(m):
            case_row.append(row[row2]*10+0)
            if row[row2]!=0:
                counting+=1
        case.append(case_row)
    # 최대 700*700 리스트 만들기(안 터지나?)
    for row in case:
        for i in range(301):
            row.insert(0,0)
            row.insert(len(row),0)
    for i in range(301):
        case.insert(0,[0 for j in range(600+m)])
        case.insert(len(case),[0 for k in range(600+m)])
    for time in range(1,k+1):
        print(time,end=' ')
        if time>100:
            x=1000
        elif time>10:
            x=100
        else:
            x=10
        for column in range(len(case)):
            for row in range(len(case[0])):
                target=case[column][row]
                vitality=target//x
                intime=target%x
                if time==10:
                    y=100
                elif time==100:
                    y=1000
                else:
                    y=x
                if vitality>0:
                    # 분열시키기
                    if time-intime==vitality+1:
                        print(vitality,end='')
                        if case[column-1][row]==0:
                            case[column-1][row]=vitality*y+time
                            counting+=1
                        if case[column+1][row]==0:
                            case[column+1][row]=vitality*y+time
                            counting+=1
                        if case[column][row+1]==0:
                            case[column][row+1]=vitality*y+time
                            counting+=1
                        if case[column][row-1]==0:
                            case[column][row-1]=vitality*y+time
                            counting+=1
                        if case[column-1][row]%y==time:
                            if case[column-1][row]//y<vitality:
                                case[column-1][row]=vitality*y+time
                        if case[column+1][row]%y==time:
                            if case[column+1][row]//y<vitality:
                                case[column+1][row]=vitality*y+time
                        if case[column][row+1]%y==time:
                            if case[column][row+1]//y<vitality:
                                case[column][row+1]=vitality*y+time
                        if case[column][row-1]%y==time:
                            if case[column][row-1]//y<vitality:
                                case[column][row-1]=vitality*y+time
                    # 죽이기
                    if vitality!=0:
                        if time-intime==vitality*2:
                            target=-1
                            counting-=1
        print()
    print(f'#{T+1} {counting}')