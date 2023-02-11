#not finished completely..............
#i will come back for u



# def binary_search(key,arr):
#     arr.sort()
#     r=len(arr)-1
#     if r<1:
#         return (-1)
#     l=0
#     mid=(l+r)/2
#     if arr[mid]==key:
#         return mid
#     elif arr[mid]>key:
#         return binary_search(key,arr)



# def find_1st_dup(arr):
#     c=0
#     i=0
#     j=len(arr)-1
#     while i<j:
#         if arr[i]==arr[j]:
#             c+=1
#             print(arr[i])
#             break
#         elif arr[i]<arr[j]:
#             j-=1
#             i+=1

#         else:
#             i+=1
#             j-=1
#     if c>0:
#         pass
#     else:
#         print(-1)

    # arr1=[0]*(max(arr)+1)
    # for i in range(len(arr)):
    #     arr1[arr[i]]+=1
    # for i in range(len(arr1)):
    #     if arr1[i]>1:
    #         # print(i)
    #         # print(f"{i} is there {arr1[i]} times")

    #         break
    #     else:
    #         c+=1
    # if c==len(arr)-1:
    #     print(-1)

def find_repeating(arr):
    c=0
    for i in range(len(arr)):
        p=binary_search(arr,arr[i],i+1,len(arr)-1)
        if p==-2:
            c+=1
        else:
            print(arr[i])
            break
    if c==len(arr)-1:
        print(-1)
    else:
        pass

def binary_search(arr,key,l,r):
    arr1=sorted(arr)
    if r<1:
        return (-2)
    else:
        mid=int((l+(r-1))/2)
        if arr1[mid]==key:
            return (key)
        elif arr1[mid]>key:
            return binary_search(arr1,key,l,mid-1)
        else:
            return binary_search(arr1,key,mid+1,r)

if __name__=="__main__":
    n=int(input("enter the lenth of the array:"))
    arr=[]
    for i in range(n):
        num=int(input("entre the number:"))
        arr.append(num)
    find_repeating(arr)