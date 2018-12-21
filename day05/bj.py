ml = []
for i in range(12):
    if i <= 6:
        if i % 2 == 0:
            ml.insert(i,31)
        elif i % 2 == 1 and i != 1:
            ml.insert(i,30)
        else:
            ml.insert(i,28)
    else:
        if i % 2 == 0:
            ml.insert(i)