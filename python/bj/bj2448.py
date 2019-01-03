import math

num = int(input())
k = math.log(num/3,2)
def star(n):
    if n == 0:
        return ['  *  ',' * * ','*****']
    else:
        startemp = []
        for i in range(len(star(n-1))):
            startemp.append(star(n-1)[i] + ' ' + star(n-1)[i])
        starall = star(n-1) + startemp
        for i in range(len(starall)):
            starall[i] = starall[i].center(len(startemp[-1]),' ')
        return starall

array = star(k)
for i in array:
    print(i)