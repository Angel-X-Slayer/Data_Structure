def binarysearch(arr1,tar,first,last):
    if first<=last:
        mid=int((first+last)/2)
        if arr1[mid]==tar:
            return(1)
        elif arr1[mid]<tar:
            return(binarysearch(arr1,tar,mid+1,last))
        else:
            return(binarysearch(arr1,tar,first,mid-1))
    else:
        return(-1)





def subarray(arr1,arr2):
    b=[]
    sum=0
    arr1=sorted(arr1)
    arr2=sorted(arr2)
    if len(arr1)==len(arr2) or len(arr1)>len(arr2):
        for i in range(len(arr2)):
            temp=binarysearch(arr1,arr2[i],0,len(arr1)-1)
            b.append(temp)
        # print(b)
        for i in range(len(b)):
            sum+=b[i]   
        if sum==len(b):
            print("yes")
        else:
            print("no")
    else:
        print("no")





# arr1=[11,1,13,21,3,7]
# arr2 = [11, 3, 7, 1]
arr1=[2]
arr2=[3]
subarray(arr1,arr2)


## sorting tao kono 1 ta function diye better hbe,quicksort in broadly used




