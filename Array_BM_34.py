## O(row*column)

def find_highest_1s(arr,n,m):
    # print(max(max(arr)))
    if max(max(arr))==0:
        print(-1)
    else:

        c_max=0
        ma=0
        for i in range(n):
            c=0
        
            for j in range(m):
                if arr[i][j]==1:
                    c+=1
                if c_max<c:
                    c_max=c
                    ma=i

        print(ma)

## O(row*log(column))  OR  O(row+column)

def find1s_binarySearch(arr,first,last):
    if arr[0]==1:
        return(0)
    else:

        if first<last:
            mid=int((first+last)/2)

            if (mid==0 or arr[mid-1]==0) and arr[mid]==1:
                return mid
            elif arr[mid]==0:
                return find1s_binarySearch(arr,mid+1,last)
            else:
                return find1s_binarySearch(arr,first,mid-1)
        return(-1)

def find1swithOnlogm(arr,n,m):
    lrow=len(arr)
    lcol=len(arr[0])
    # print(lrow)
    max_1s=0
    num_of_row=-1
    for i in range(0,lrow):
        idx=find1s_binarySearch(arr[i],0,lcol-1)
        num_of_1=lcol-idx
        if idx!=-1 and num_of_1>max_1s:
            max_1s=num_of_1
            num_of_row=i
    print(num_of_row)

## O(row+column)



arr=([
        [0,0],
        [0,0]
        # [0,1,1,1],
        # [0,0,1,1],
        # [1,1,1,1],
        # [0,0,0,0]
    ])
# mat=len(arr)
# pik=len(arr[0])
# print(pik)
# print(mat)
m=2
# m=4
# n=4
n=2
# find_highest_1s(arr,n,m)
find1swithOnlogm(arr,n,m)


## m=row
## n=column
## len(arr) is used for finding the number of rows in the matrix
## len(arr[0]) is used to find the numver of columns in the matrix