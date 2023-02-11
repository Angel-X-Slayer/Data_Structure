def find_longest_subsequence(arr):
    n=len(arr)
    m=max(arr)
    # print(m)
    maxi=0
    c=0
    b=[0]*(m+1)
    # print(b)
    for i in range(n):
        b[arr[i]]=1
    i=0
    while i<len(b):
        if b[i]==1:
            c+=1
            i+=1
        else:
            c=0
            i+=1
        if c>maxi:
            maxi=c
    print(maxi)

# arr=[2,6,9,1,4,5,3]
arr=[1,9,3,10,4,20,2]
find_longest_subsequence(arr)