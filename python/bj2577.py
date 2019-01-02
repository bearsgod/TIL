import sys

a = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())
c = int(sys.stdin.readline().strip())

num = a * b * c
countnum = str(num)
for i in range(10):
    print(countnum.count(str(i)))