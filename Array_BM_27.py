## O(nk) tym complexity & O(nk) extra space

def find_ele(arr,k,n):
    arr1=[0]*(max(arr)+1)
    # print(arr1)
    for i in range(len(arr)):
        arr1[arr[i]]+=1
    for i in range(len(arr1)):
        if arr1[i]>int(n/k):
            print(i)

## O(nlogn) tym complexity and O()

def find_elements(arr,k,n):
    # print(type(arr))
    # print(type(n))
    # print(type(k))
    first=0
    last=n-1
    count=1
    # print(arr)

    arr1=quicksort(arr,first,last)
    # print(arr1)
    # print(arr1)
    # arr1=sorted(arr)
    # print(arr1)
    for i in range(len(arr1)-1):
        if arr1[i]==arr1[i+1]:
            count+=1
        else:
            c=1
        if count>int(n/k):
            print (arr1[i])
            count=1
                
                

            



def quicksort(arr,first,last):
    if first<last:
        p=findpivot(arr,first,last)
        quicksort(arr,first,p-1)
        quicksort(arr,p+1,last)
    return(arr)


def findpivot(arr,first,last):
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
            arr[left],arr[right]=arr[right],arr[left]
    arr[last],arr[left]=arr[left],arr[last]
    return (left)










if __name__=="__main__":
    arr=[]
    n=int(input("enter the lenth of the array:"))
    k=int(input("enter the value of k:"))
    for i in range(n):
        num=int(input("enter the number:"))
        arr.append(num)
    # print(type(arr))
    # print(type(k))
    # print(type(n))
    find_elements(arr,k,n)    