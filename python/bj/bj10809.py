S = input()
al = ''
for i in range(97,123):
    al += (str(S.find(chr(i))) + ' ')
print(al[0:-1])