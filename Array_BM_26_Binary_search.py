##this is O(n) tym complexity. because we iterate through the whole array once.

def find_min_rotated_sorted(arr):
    for i in range(len(arr)):
        if arr[i]<arr[i+1]:
            pass
        else:
            print(arr[i+1])
            break

## this is O(n) tum complexity

def findmin(arr,low,high):
    mid=int((low+high)/2)
    if high<low:
        return(arr[0])
    if high==low:
        return(arr[low])
    if mid < high and arr[mid] < arr[high]:
        return findmin(arr,0,mid)
    else:
        return findmin(arr,mid+1,high)
    # if arr[high] > arr[mid]:
    #     return findmin(arr, low, mid-1)
    # return findmin(arr, mid+1, high)

    


if __name__=="__main__":
    arr=[]
    low=0
    n=int(input("entre the lenth of the aray:"))
    high=n-1
    for i in range(n):
        num=int(input("enter the number:"))
        arr.append(num)
    print(findmin(arr,low,high))

    ## this algorithem is basically based on the binary search technique
    ## it is also a divide and concorer technique
    ## we divide the the list baesd on a mid element,then check if the mid is less than the prev or greater than nxt
    ## then check if mid is less than high or not if so then recursively implement findmin on the right list
    ## otherwise in the left side
    ## return the result  
