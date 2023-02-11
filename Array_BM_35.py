def array_spiral(arr,m,n,k,l):
    i,j=0,0
    while m<n and k<l:
        for j in range(l):
            print(arr[m][j], end=" ")
        m+=1
        for i in range(m,n):
            print(arr[i][l-1],end=" ")
        l-=1
        if k<l:
            for j in range(l-1,k-1,-1):
                print(arr[n-1][j],end=" ")
            n-=1
        if m<n:
            for i in range(n-1,m-1,-1):
                print(arr[i][k],end=" ")
            k+=1

arr=([
        # [0,0],
        # [0,0]
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16],
        [17,18,19,20]
    ])
m=0
n=5
k=0
l=4
array_spiral(arr,m,n,k,l)


## start of row=m
## end of row=n
## start of column=k
## end of column=l
## row itrator=i
## column itrator=j
## in case of 3X2 matrix; m=0_n=3_k=0_l=2