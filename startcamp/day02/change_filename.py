import os

os.chdir(r'C:\Users\student\ysw\day02\dummy')
# print(os.getcwd())
for filename in os.listdir('.'):
    os.rename(filename, filename.replace('지원자_지원자_','합격자_'))

# 합격자_0_누구누구.txt