def partition(arr,fisrt,last):
    pivot=fisrt
    p=-1
    left=fisrt
    right=last
    while left<right:
        if arr[left]<pivot:
            p+=1
            arr[p],arr[left]=arr[left],arr[p]
            left+=1
        else:
            left+=1
    return (arr,p)

def alternative_pos_neg(arr):
    first=0
    last=len(arr)-1
    arr1,po=partition(arr,first,last)
    # print(arr)
    # print()
    # print(po)
    neg=0
    pos=po+1
    while neg!=pos:
        arr1[neg],arr1[pos]=arr1[pos],arr1[neg]
        neg+=2
        pos+=1
    print(arr1)
    # arr1=[]
    # k=0
    # for i in range(len(arr)):
    #     if arr[i]>=0:
    #         arr1.append(arr[i])
    #         k=i
    # for i in range(len(arr)):
    #     if arr[i]<0:    
if __name__=="__main__":
    n=int(input("nter the lenth of the array:"))
    arr=[]
    for i in range(n):
        num=int(input("enter the numbers:"))
        arr.append(num)
    alternative_pos_neg(arr)

# the time complexity of the optimal solution is O(n)
# the space complexity of the optimal solution is O(1)
# the algotithem is based on two parts, the 1st part is a changed copy of partitioning function from quicksort.
# Here we take the pivot as 0, and then check if the left idxed value is less than or greater than pivot.
# if the value is less than pivot then p in incremented, and swap between a[p] and a[left], then left increment.
# else only left is incremented.
# after terminating from the while loop,return the value of p and array.
# in the function alternative_pos_neg , neg=0 and pos=p+1.
# swap a[neg] and a[pos] then increment pos by 1 and neg by 2.
# after teminating from the loop print the new array.