import sys

string = sys.stdin.readline().strip()
count = string.split(' ')
num = len(count)
for i in count:
    if i is '':
        num -= 1
print(num)