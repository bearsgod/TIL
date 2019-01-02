# f = open('ssafy.txt','w') # w: write, r: read, a: append
# f.write('This is SSAFY!')
# f.close()


with open('ssafy.txt','r',encoding='utf8') as f:
    lines = f.readlines()

lines.reverse()


with open('ssafy_reverse.txt','w',encoding='utf8') as f:
    f.writelines(lines)
    # for i in range(10):
    #     f.write(f'This is \'SSAFY\'! {i}\n')
        # \t : tab, \\ : '\' 문자, \' & \" : 따옴표, 쌍따옴표 문자

# lines = ['1\n','2\n','3\n']
# rlines = reversed(lines)

# with open('ssafy.txt','w',encoding='utf8') as f:
#     f.writelines(lines)

# with open('ssafy_reverse.txt','w',encoding='utf8') as f:
#     f.writelines(rlines)