l = []
for i in range(5):
    l.append(int(input()))
score = 0
for item in l:
    if item < 40:
        item = 40
        score += item
    else:
        score += item
avg = score/5
print(int(avg))