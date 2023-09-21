# graph = [[0, 1000, 2000],
#          [0, 0, 5000],
#          [0, 0, 0]]
graph = [[0, 1000, 2000, 0],
         [0, 0, 3000, 1000],
         [0, 0, 0, 8000],
         [2000, 3000, 2000, 0]]
op = [0]*len(graph)
# print(op)
for i in range(len(graph)):
    for j in range(len(graph)):
        if (graph[i][j] != 0):
            op[i] -= graph[i][j]
            op[j] += graph[i][j]
maxi = op.index(max(op))
for i in range(len(op)):
    if op[i] < 0:
        print(f"{i} ows {abs(op[i])} to {maxi}")
