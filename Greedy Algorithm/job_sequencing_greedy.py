arr = [['a', 2, 100],  # Job Array
       ['b', 1, 19],
       ['c', 2, 27],
       ['d', 1, 25],
       ['e', 3, 15]]
arr = sorted(arr, key=lambda x: x[2], reverse=True)
f = 0
op = []
for i in range(len(arr)):
    if f <= arr[i][1]:
        op.append(arr[i][0])
        f += 1
[print(i) for i in op]
