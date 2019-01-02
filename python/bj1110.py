import sys

n = int(sys.stdin.readline())
cyclen = n
newn = 0
cycle = 0
while n != newn:
    cycle += 1
    addn = (cyclen % 10) + (cyclen // 10)
    newn = (addn % 10) + ((cyclen % 10) * 10)
    cyclen = newn
if n == 0:
    cycle = 1
print(cycle)