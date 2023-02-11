def alternating(arr):
    n=len(arr)
    c=2
    c_max=0
    for i in range(1,n-1):
        if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
            c+=1
        elif arr[i]<arr[i-1] and arr[i]<arr[i+1]:
            c+=1
        if c>c_max:
            c_max=c
    print(c_max)

# nums = [1,5,4]
# nums=[1,17,5,10,13,15,10,5,16,8]
nums=[10, 22, 9, 33, 49, 50, 31, 60]
alternating(nums)
        
    