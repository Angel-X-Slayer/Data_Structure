arr = [[60, 10], [100, 20], [120, 30]]
w = 50

# arr = [[500, 30]]
# w = 10


weight = 0
profit = 0
arr = sorted(arr, key=lambda x:
             x[0]/x[1], reverse=True)
for i in arr:
    if w-weight == 0 or w == 0:
        break
    if i[1] > w:
        profit += (w/i[1])*i[0]
        weight += ((w/i[1])*i[1])
        break
    elif i[1] <= w-weight and w-weight != 0:
        profit += i[0]
        weight += i[1]
    elif i[1] > w-weight and w-weight != 0:
        profit += ((w-weight)/weight)*i[0]
        weight += ((w-weight)/weight)*i[1]
# if type(profit) == float:

#     print(round(profit, 2))
# else:
#     print(profit)

print(round(profit, 2))
