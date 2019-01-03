n = int(input())
number = n
for i in range(n):
    s = input()
    t = 0
    for j in range(97,123):
        c = s.count(chr(j))
        if c > 1:
            re = s.find(chr(j))
            for k in range(c):
                if s[re + k] != s[re]:
                    t = 1
    number -= t

print(number)