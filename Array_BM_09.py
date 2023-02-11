def neg_move(arr):
    i=0
    for i in range(len(arr)):
        mi=i
        for j in range(i+1,len(arr)):
            if arr[mi]>arr[j]:
                mi=j
        arr[mi],arr[i]=arr[i],arr[mi]
    return(arr)

if __name__=="__main__":
    n=int(input("enter the lmt:"))
    arr=[]
    for i in range(n):
        num=int(input("enter the nuber:"))
        arr.append(num)
    arr=neg_move(arr)
    print(arr)

