import math

num = int(input())
k = math.log(num/3,2)
def star(n):
    base = int((2**n)*5 + (2**n)-1)
    if n == 0:
        return ['  *  ',' * * ','*****']
    else:
        basement = star(n-1)
        startemp = []
        for i in range(len(basement)):
            startemp.append(basement[i] + ' ' + basement[i])
        starall = basement + startemp
        for i in range(len(starall)):
            starall[i] = starall[i].center(base,' ')
        return starall

array = star(k)
for i in array:
    print(i)