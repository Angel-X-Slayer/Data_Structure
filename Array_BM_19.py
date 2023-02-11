def quicksort(arr,low,high):
    if low<high:
        p=find_pivot(arr,low,high)
        quicksort(arr,low,p-1)
        quicksort(arr,p+1,high)

def find_pivot(arr,low,high):
    pi=arr[high]
    left=low
    right=high-1
    while True:
        while left<=right and arr[left]>=arr[high]:
            left+=1
        while arr[right]<=arr[high] and left<=right:
            right-=1
        if right<left:
            break
        else:
            arr[left],arr[right]=arr[right],arr[left]
    arr[high],arr[left]=arr[left],arr[high]
    return(left)

if __name__=="__main__":
    x=int(input("enter the target:")) 
    n=int(input("enter the lenth:"))
    arr=[]
    for i in range(n):
        num=int(input("enter the number:"))
        arr.append(num)
    quicksort(arr,0,n-1)
    for i in range(x):
        print(arr[i])