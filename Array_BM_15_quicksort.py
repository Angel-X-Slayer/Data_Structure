def partition(arr,first,last):
## def find_pivot(arr,first,last):
    pi=arr[last]
    left=first
    right=last-1
    while True:
        while left<=right and arr[left]<=arr[last]:
            left=left+1
        while left<=right and arr[right]>=arr[last]:
            right=right-1

        if right<left:
            break
        else:
            arr[left],arr[right]=arr[right],arr[left]
    arr[last],arr[left]=arr[left],arr[last]
    return left

def quicksort(arr,first,last):
    if first<last:
        p=partition(arr,first,last)
        quicksort(arr,first,p-1)
        quicksort(arr,p+1,last)
    return(arr)
    
if __name__=="__main__":
    arr=[]
    n=int(input("enter the lenth of the array:"))
    for i in range(n):
        num=int(input("enter the nymber:"))
        arr.append(num)
    c=quicksort(arr,0,n-1)
    print(c)


    