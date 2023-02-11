def Findoccuring(arr,key):
    cou=0
    for i in range(len(arr)):
        if arr[i]==key:
            cou+=1
    return(cou)

if __name__=="__main__":
    key=int(input("enter the key:"))
    n=int(input("enter the limit:"))
    arr=[]
    for i in range(n):
        num=int(input("enter the number:"))
        arr.append(num)
    cou=Findoccuring(arr,key)
    print(cou)
        