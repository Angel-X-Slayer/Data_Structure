# def non_repeating(arr):
#     arr.sort()
#     arr1=[0]*(max(arr)+1)
#     for i in range(len(arr)):
#         arr1[arr[i]]+=1
#     for i in range(len(arr1)):
#         if arr1[i]==1:
#             print(i)
#             print(f"{i} is there {arr1[i]} times")
#             break


# if __name__=="__main__":
#     n=int(input("enter the lenth of the array:"))
#     arr=[]
#     for i in range(n):
#         num=int(input("entre the number:"))
#         arr.append(num)
#     non_repeating(arr)

def find_repeating(arr):
    for i in range(len(arr)):
        p=binary_search(arr,arr[i],0,len(arr)-1)
        if p=="c":
            print(arr[i])
            break
        else:
            pass

def binary_search(arr,key,l,r):
    arr1=sorted(arr)
    if r<1:
        return ("c")
    else:
        mid=int((l+r)/2)
        if arr1[mid]==key:
            return (key)
        elif arr1[mid]>key:
            return binary_search(arr1,key,0,mid-1)
        else:
            return binary_search(arr1,key,mid+1,r)

if __name__=="__main__":
    n=int(input("enter the lenth of the array:"))
    arr=[]
    for i in range(n):
        num=int(input("entre the number:"))
        arr.append(num)
    find_repeating(arr)