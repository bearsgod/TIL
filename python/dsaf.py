def fib_loop(n):
    fl = [1,1]
    for i in range(3,n+2):
        f = fl[n-3]+fl[n-2]
        fl.append(f)
    return f

print(fib_loop(10))