def binarysearch(key,arr,r,l):
    mid=r+(l-1)//2
    if arr[mid]==key:
        #return arr[mid], # this return statement is for this programme
        return(1)

    if arr[mid]<key:
        binarysearch(key,arr,mid+1,l-1)
    elif arr[mid]>key:
        binarysearch(key,arr,0,mid-1)
    else:
        return(-1)

def selection_sort(arr):
    i=0
    for i in range(len(arr)):
         mi=i
         for j in range(i+1,len(arr)):
             if arr[mi]>arr[j]:
                 mi=j
         arr[mi],arr[i]=arr[i],arr[mi]
    return(arr)

def uni(arr1,arr2):
    arr1=list(set(selection_sort(arr1)))
    arr2=list(set(selection_sort(arr2)))
    i,j=0,0
    k=0
    arr3=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            arr3.append(arr1[i])
            i+=1

        elif arr1[i]>arr2[j]:
            arr3.append(arr2[j])
            j+=1
        else:
            arr3.append(arr2[j])
            i+=1
            j+=1

    while i<len(arr1):
        arr3.append(arr1[i])
        i+=1
    while j<len(arr2):
        arr3.append(arr2[j])
        j+=1
    print(arr3)
    

def inter(arr1,arr2):
    arr1=selection_sort(arr1)
    arr2=selection_sort(arr2)
    arr4=[]
    # if len(arr1)==len(arr2):
    #     for i in range(len(arr1)):
    #         s=binarysearch(arr1[i],arr2,0,len(arr2))
    #         arr4.append(s)
    # elif len(arr1)<len(arr2):
    #     for i in range(len(arr1)):
    #         s=binarysearch(arr1[i],arr2,0,len(arr2))
    #         arr4.append(s)
    # else:
    #     for i in range(len(arr2)):
    #         s=binarysearch(arr2[i],arr1,0,len(arr1))
    #         arr4.append(s)
    # print(arr4)


    
    i,j=0,0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]==arr2[j]:
            arr4.append(arr1[i])
            i+=1
            j+=1
        elif arr1[i]<arr2[j]:
            i+=1
        else:
            j+=1
    print(arr4)

    

if __name__=="__main__":
    n1=int(input("enter the lim for array 1:"))
    arr1=[]
    for i in range(n1):
        num=int(input("enter the nuber:"))
        arr1.append(num)
    n2=int(input("enter the lim for array 2:"))
    arr2=[]
    for j in range(n2):
        num=int(input("enter the nuber:"))
        arr2.append(num)
    uni(arr1,arr2)
    inter(arr1,arr2)




    


    
