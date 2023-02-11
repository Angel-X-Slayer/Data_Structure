def Findminmax(arr):
    n=len(arr)
    min=arr[0]
    max=arr[n-1]
    for i in range(1,n):
        if arr[i]<=min:
            min=arr[i] 
        elif arr[i]>=max:
            max=arr[i]
    print(f"the maximum number is {max} and the minimum number is {min}")

if __name__=="__main__":
    lm=int(input("enter the limit:"))
    arr=[]
    for i in range(lm):
        num=int(input("enter the nuber:"))
        arr.append(num)
    Findminmax(arr)
