def Sort012(arr):
    i=0
    for i in range(len(arr)):
        mi=i
        for j in range(i+1,len(arr)):
            if arr[mi]>arr[j]:
                mi=j
        arr[i],arr[mi]=arr[mi],arr[i]
    return arr
if __name__=="__main__":
    n=int(input("enter the limit:"))
    arr=[]
    for i in range(n):
        num=int(input("enter the number:"))
        arr.append(num)
    s=Sort012(arr)
    print(s)