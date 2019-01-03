casenum = int(input())
for i in range(casenum):
    case = input()
    repeat, string = case.split(' ')
    repeatnum = int(repeat)
    makestr = ''
    for j in string:
        makestr += j * repeatnum
    print(makestr)