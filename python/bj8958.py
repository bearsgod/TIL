import sys

casenum = int(sys.stdin.readline().strip())
for i in range(casenum):
    case = sys.stdin.readline().strip()
    realcase = case.split('X')
    score = 0
    for j in realcase:
        onum = j.count('O')
        if onum != 0:
            score += sum(range(1,onum+1))
    print(score)