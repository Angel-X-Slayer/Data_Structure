def findpivot(arr,l,r):
    pivot=r
    left=l
    right=r-1
    while True:
        while left<=right and arr[left]<=arr[pivot]:
            left+=1
        while left<=right and arr[right]>=arr[pivot]:
            right-=1
        if right<left:
            break
        else:
            arr[right],arr[left]=arr[left],arr[right]
    arr[left],arr[pivot]=arr[pivot],arr[left]
    return(left)





def quicksort(arr,l,r):
    if l<r:
        p=findpivot(arr,l,r)
        quicksort(arr,l,p-1)
        quicksort(arr,p+1,r)
    return(arr)


# def smllst_pos_inte(arr):
#     l=0
#     r=len(arr)-1
#     arr=quicksort(arr,l,r)
#     for i in range(len(arr)):
#         if arr[i]==1:
#             if arr[i+1]!=2:
#                 return(2)
#                 break
#         else:




# arr=[2,6,1,9,4,5,3]
# smllst_pos_inte(arr)


## .........................***************************........................ ##



def findSmallest(arr, n):
	arr=quicksort(arr,0,n-1)

	res = 1 
	for i in range (0, n ):
		if arr[i] <= res:
			res = res + arr[i]
		else:
			break
	return res


# Driver program to test above function
arr1 = [1, 3, 4, 5]
n1 = len(arr1)
print(findSmallest(arr1, n1))

arr2= [1, 2, 6, 10, 11, 15]
n2 = len(arr2)
print(findSmallest(arr2, n2))

arr3= [1, 1, 1, 1]
n3 = len(arr3)
print(findSmallest(arr3, n3))

arr4 = [1, 2, 3, 4]
n4 = len(arr4)
print(findSmallest(arr4, n4))

# This code is.contributed by Smitha Dinesh Semwal






















