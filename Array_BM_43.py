from collections import *

## tym complexity O(nlogn) 
## no xtra sps taken


def MS(arr):
    if len(arr)>1:
        mid=len(arr)//2
        l=arr[:mid]
        r=arr[mid:]
        MS(l)
        MS(r)
        i=j=k=0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                arr[k]=l[i]
                i+=1
            else:
                arr[k]=r[j]
                j+=1
            k+=1
        while i<len(l):
            arr[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            arr[k]=r[j]
            j+=1
            k+=1
        return arr

def missing_repeating(arr):
    arr1=MS(arr)
    # print(arr1)
    p,l=1,1
    for i in range(len(arr)-1):
        if arr[i+1]!=arr[i]+1:
            print("the missing element is", arr[i]+1)
            break
            
        else:
            p+=1
    # print(p)
    if p==len(arr):
        print("no missin elemenet")
    else:
        pass
    for i in range(len(arr)-1):
        if arr[i+1]==arr[i]:
            print("the repeating element is" ,arr[i])
            break
        else:
            # print("no repeating element")
            l+=1
    # print(l)
    if l==len(arr):
        print("no repeatin element")
    else:
        pass

# def missin_repeatin_hashin(arr):
#     c=Counter(arr)
#     print(c)




# arr=[1,3,3]
arr=[1,3,5,4,2]
# arr=[1,2,2]
# arr=[1,3]
missing_repeating(arr)
# missin_repeatin_hashin(arr)
