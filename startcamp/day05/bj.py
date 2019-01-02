import sys

num = sys.stdin.readline().strip()
renum = 0
trynum = 0
while renum != num:
    if len(num) == 1:
        num = '0' + num
    sumnum = str(int(num[0])+int(num[1]))
    if len(sumnum) == 1:
        sumnum = '0' + sumnum
    renum = num[1] + sumnum[1]
    trynum += 1
print(trynum)
