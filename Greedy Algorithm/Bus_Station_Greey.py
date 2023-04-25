# arr = [100, 300, 500]
# dep = [900, 400, 600]
# arr = [900, 940, 950, 1100, 1500, 1800]
# dep = [910, 1200, 1120, 1130, 1900, 2000]
arr = [900, 940]
dep = [910, 1200]
z = list(zip(arr, dep))
# print(z)
op = 1
i = 1
k = z[0][1]
while i < (len(z)):
    if i != len(z)-1:
        if z[i][0] > k:
            k = z[i][1]
            op += 0
            i += 1
        else:
            op += 1
            i += 1
    else:
        i += 1
print(op)


# zip arr and dep array. Then check if the dep of a train is less than the next trains arrivl.
# if so no need to increase the op. if the arraival time of the next train in less than the dep time
# of this train then set the dep time as k and check if the arraivals are less than k then increment op,
# otherwise just increment i.
