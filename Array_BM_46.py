def sorte(arr):
    # print(arr)
    if len(arr)>1:
        mid=len(arr)//2
        L=arr[ :mid]
        R=arr[mid: ]
        sorte(L)
        sorte(R)
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1
        return(arr)



def find_min_diff(arr,m):
    arr=sorte(arr)
    # i=0
    # j=len(arr)-1
    diff=1000000000000000000
    # while i<j:
    #     if arr[j]-arr[i]>m and arr[j]-arr[i]<diff:
    #         diff=arr[j]-arr[i]
    #         j-=1
    #     else:
    #         i+=1
    # print(diff)
    for i in range(len(arr)-1):
        j=i+(m-1)
        if j<=len(arr)-1 and arr[j]-arr[i]<diff:
            diff=arr[j]-arr[i]
    print(diff)


















# arr=[3,4,1,9,56,7,9,12]
# m=5
# arr=[7, 3, 2, 4, 9, 12, 56]
# m=3
arr=[12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
m=7
find_min_diff(arr,m)