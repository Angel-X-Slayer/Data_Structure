def maxofproduct(arr):
    prod=1
    max_prod=min(arr)
    i=0
    j=len(arr)
    while i<j:
        prod=prod*arr[i]
        if prod>max_prod:
            max_prod=prod
        if prod==0:
            prod=0
        i+=1
    print(max_prod)

if __name__=="__main__":
    n=int(input("enter the lenth of the array:"))
    arr=[]
    for i in range(n):
        num=int(input("enter the number:"))
        arr.append(num)
    maxofproduct(arr)