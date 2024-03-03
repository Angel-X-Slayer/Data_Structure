def xpown(x, n):
    if x == 1:
        return (1)
    elif n == 0:
        return (1)
    else:
        return (x*xpown(x, n-1))


x = 2
n = 3
k = xpown(2, 3)
print(k)
