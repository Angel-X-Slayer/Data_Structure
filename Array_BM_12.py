def find_missing_int(arr):
    mi=arr[0]
    ma=arr[0]
    for i in range(1,len(arr),1):
        if arr[i]>ma:
            ma=arr[i]
        elif arr[i]<mi:
            mi=arr[i]
    j,k=0,0
    for i in range(mi,ma+1):
        j=j+i
    for i in range(len(arr)):
        k=k+arr[i]
    mis=j-k
    print(mis)
if __name__=="__main__":
    arr=[]
    n=int(input("enter the lenth of the array:"))
    for i in range(n):
        num=int(input("enter the number:"))
        arr.append(num)
    find_missing_int(arr)
        