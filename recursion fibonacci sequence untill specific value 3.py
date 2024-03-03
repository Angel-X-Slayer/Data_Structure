def fibonacci(n):
    if n == 1:
        return (0)
    elif n == 2:
        return (1)
    else:
        return (fibonacci(n-1)+fibonacci(n-2))


n = 10
target = 17
arr = []
for i in range(1, n+1):
    k = fibonacci(i)
    if k < target:
        arr.append(k)
    else:
        break
print(arr)
