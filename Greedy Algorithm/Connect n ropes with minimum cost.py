import heapq
arr = [4, 3, 2, 6]
N = 4
heapq.heapify(arr)
k = 0
while len(arr) > 1:
    first = heapq.heappop(arr)
    second = heapq.heappop(arr)
    k += first+second
    t = first+second
    heapq.heappush(arr, t)
print(k)
# print(arr)
