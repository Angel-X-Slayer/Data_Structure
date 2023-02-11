def wavearray(arr):
    i=0
    if (len(arr)-1)%2==0:
        while i<len(arr)-2:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            i+=2
    else:
        while i<len(arr)-1:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            i+=2
    print(arr)

# arr=[1,2,3,4,5]
arr=[2,4,7,8,9,10]

wavearray(arr)
