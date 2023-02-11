def ran_coeff(arr):
    min=arr[0]
    max=arr[len(arr)-1]
    for i in range(1,len(arr),1):
        if arr[i]<=min:
            min=arr[i] 
        elif arr[i]>=max:
            max=arr[i]
    ran=max-min
    coeff=ran/(max+min)
    print(ran,coeff)

if __name__=="__main__":
    n=int(input("enter the lmt:"))
    arr=[]
    for i in range(n):
        num=int(input("enter the nuber:"))
        arr.append(num)
    ran_coeff(arr)
