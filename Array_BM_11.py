def rotating(arr):
    n=len(arr)
    x = arr[n - 1]
     
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
         
    arr[0] = x
    return (arr)

if __name__=="__main__":
    arr=[]
    n=int(input("enter the lenth of the array:"))
    for i in range(n):
        num=int(input("enter the number:"))
        arr.append(num)
    arr1=rotating(arr)
    print(arr1)

##  right shift by 1
             
