def max(a, b):
    if(a > b):
        return a
    else:
        return b
def min(a, b):
    if(a < b):
        return a
    else:
        return b
def maxIndexDiff(arr, n):
    LMin = [0] * n
    RMax = [0] * n
    LMin[0] = arr[0]
    for i in range(1, n):
        LMin[i] = min(arr[i], LMin[i - 1])
    # print(LMin)
    RMax[n - 1] = arr[n - 1]
    for j in range(n - 2, -1, -1):
        RMax[j] = max(arr[j], RMax[j + 1])
    # print(RMax)
    i, j = 0, 0
    maxDiff = -1
    while (j < n and i < n):
        if (LMin[i] <= RMax[j]):
            maxDiff = max(maxDiff, j - i)
            
            j = j + 1
        else:
            i = i + 1
    return maxDiff
if(__name__ == '__main__'):
    arr = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
    n = len(arr)
    maxDiff = maxIndexDiff(arr, n)
    print (maxDiff)

