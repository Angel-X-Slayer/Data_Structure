def find_pivot(arr,first,last):
    pivot=arr[last]
    left=first
    right=last-1
    while True:
        while left<=right and arr[left]<=pivot:
            left+=1
        while left<=right and arr[right]>=pivot:
            right-=1
        if right<left:
            break
        else:
            arr[right],arr[left]=arr[left],arr[right]
    arr[last],arr[left]=arr[left],arr[last]
    # print(arr)
    return(left)





def quicksort(arr,first,last):
    if first<last:
        p=find_pivot(arr,first,last)
        quicksort(arr,first,p-1)
        quicksort(arr,p+1,last)
    return(arr)



def largest_consecutive_sub(arr):
    arr1=quicksort(arr,0,len(arr)-1)
    print(arr1)
    c=1
    c_max=0
    for i in range(len(arr1)-1,0,-1):
        if arr1[i-1]==arr1[i]-1:
            c+=1
        else:
            c=1


        if c>c_max:
            c_max=c
    print(c_max)


    # first=0
    # last=len(arr)-1
    # arr=quicksort(arr,first,last)
    # print(arr)
    # print(first,last)

if __name__=="__main__":
    arr=[]
    n=int(input("enter the lenth of the array:"))
    for i in range(n):
        num=int(input("enter the number:"))
        arr.append(num)
    # arr1=sorted(arr)
    # print(arr1)
    largest_consecutive_sub(arr)
    # quicksort(arr,0,n-1)
    # print(arr)