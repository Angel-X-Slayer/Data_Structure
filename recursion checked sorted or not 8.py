def check_soreted(arr, flag, idx):
    if idx == len(arr)-1:
        return flag
    else:
        if arr[idx] < arr[idx+1] and flag == 0:
            return (check_soreted(arr, flag, idx+1))
        else:
            flag = 1
            return


arr = [1, 2, 3, 4]
flag = 0
k = check_soreted(arr, flag, 0)
if k == 0:
    print("sorted")
else:
    print("Not sorted")
