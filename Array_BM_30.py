def min_jump(arr,n):
    c=0
    temp=0
    i=0
    while i<n-1:
        if arr[i]==0:
            return(-1)
            break
        else:
            temp=arr[i]
            i+=temp
            c+=1
    return(c)

if __name__=="__main__":
    n=int(input("enter the lenth of the array:"))
    arr=[]
    for i in range(n):
        num=int(input("enter the number:"))
        arr.append(num)
    print(min_jump(arr,n))
        