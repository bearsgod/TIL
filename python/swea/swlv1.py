# # sw 2072
# for i in range(int(input())):
#     l = input().split(' ')
#     a = 0
#     for j in l[0:10]:
#         if int(j) % 2:
#             a += int(j)
#     print(f'#{i} {a}')

# # sw 1545
# for i in range(int(input()),-1,-1):
#     print(i,end=' ')

# # sw 2019
# for i in range(int(input())+1):
#     print(2**i,end=' ')

# # sw 1936
# l = ['3 2','2 1','1 3']
# if input() in l:
#     print('A')
# else:
#     print('B')

# # sw 1933
# n=int(input())
# for i in range(n):
#     if n%(i+1)==0:
#         print(i+1,end=' ')

# # sw 1938
# a,b = input().split(' ')
# x,y = int(a),int(b)
# c,d,e,f = x+y,x-y,x*y,int(x/y)
# print(c,d,e,f,sep='\n')

# # sw 2025
# print(sum(list(range(int(input())+1))))

# # sw 2027
# print("""#++++
# +#+++
# ++#++
# +++#+
# ++++#""")

# # sw 2029 
# for i in range(int(input())):
#     a,b=map(int,input().split(' '))
#     print(f'#{i+1} {a//b} {a%b}')

# # sw 2043
# a,b=map(int,input().split(' '))
# print(a-b+1)

# # sw 2046
# print('#'*int(input()))

# # sw 2047
# print(input().upper())

# # sw 2050
# [print(i,end=' ') for i in list(map(lambda x:ord(x)-64,list(input()[::1])))]

# # sw 2056
# l=[31,28,31,30,31,30,31,31,30,31,30,31]
# n=int(input())
# for i in range(n):
#     d=input()
#     m=d[4:6]
#     o=d[6:8]
#     if int(m)>12 or int(m)<=0 or int(o)>l[int(m)-1] or int(o)<=0:
#         print(f'#{i+1} -1')
#     else:
#         print(f'#{i+1} {d[0:4]}/{m}/{o}')

# # sw 2058
# print(sum(map(int,input()[::1])))

# # sw 2063
# n = int(input())
# l = list(map(int,input().split(' ')))
# l.sort()
# print(l[int((n+1)/2-1)])

# # sw 2068
# for i in range(int(input())):
#     print(f'#{i+1} {max(map(int,input().split()))}')

# # sw 2070
# n = int(input())
# for i in range(n):
#     a,b = map(int,input().split())
#     c = ''
#     if a > b:
#         c = '>'
#     elif a == b:
#         c = '='
#     else:
#         c = '<'
#     print(f'#{i+1} {c}')

# # sw 2071
# for i in range(int(input())):
#     print(f'#{i+1} {round(sum(map(int,input().split()))/10)}')