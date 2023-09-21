def findMinTime(k, T, job, n):
    res = []
    subset = [0]*100

    def dfs(i):
        if i >= n:
            res.append(subset)
            return
        for j in job:
            subset[i] += job[i]
        dfs(i+1)

        pass
    dfs(0)
    pass


job = [10, 7, 8, 12, 6, 8]
n = len(job)
k = 4
T = 5
print(findMinTime(k, T, job, n))
# def possibility(arr):
#     res=[]
#     subset=[]
#     def dfs(i):
#         if i>=len(arr):
#             res.append(subset.copy())
#             return
#         res.append(arr[i])
#         dfs(i+1)
#         subset.pop()
#         dfs(i+1)
#     dfs(0)
#     print(res)

# arr=[1,2,3]
# possibility(arr)
