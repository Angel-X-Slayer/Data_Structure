def fibonacci(n):
    if n == 1:
        return (0)
    elif n == 2:
        return (1)
    else:
        return (fibonacci(n-1)+fibonacci(n-2))


n = 5
arr = []
for i in range(1, n+1):
    k = fibonacci(i)
    arr.append(k)
print(arr)
