def duplicate(arr):
    arr1=[0]*1000
    for i in range(len(arr)):
        arr1[arr[i]]+=1
    for i in range(len(arr1)):
        if arr1[i]==0 or arr1[i]==1:
            pass
        else:
            print(f"there is {arr1[i]} {i}s")

if __name__=="__main__":
    arr=[]
    n=int(input("enter the lenth of the array:"))
    for i in range(n):
        num=int(input("enter the number:"))
        arr.append(num)
    duplicate(arr)