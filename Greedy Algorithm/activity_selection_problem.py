start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
lst = list(zip(start, finish))
# print(lst)
# lst = sorted(lst, key=lambda x: x[0])      ## sort 2 lists with the help of 1st list elements
# print(lst)
op = []
f = 0
for i in range(len(lst)):
    if len(op) == 0:
        op.append(i)
        f = lst[i][1]
    else:
        if lst[i][0] > f:
            op.append(i)
            f = lst[i][1]
print(op)


# f is the ending poibnt of a task. if f is less thanm the next task, then append the index of the task in op,
# and update the f with recent task's ending time. if the f is greater than the starting time of the next task then pass
# and go to the next task.


# https://www.geeksforgeeks.org/top-20-greedy-algorithms-interview-questions/
