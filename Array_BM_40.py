## O(n) tym complexity but no extra space taken  


def secnd_largest(arr):
    i,maxi,p,c=0,0,0,0
    n=len(arr)
    while i<n:
        if arr[i]>maxi:
            maxi=arr[i]
        i+=1
    max2=maxi
    for i in range(n):
        if arr[i]==maxi:
            pass
        else:
            p=maxi-arr[i]
            if p<max2:
                max2=p
                c=arr[i]
    return(c)


def trappingWater(arr):
    larg2=secnd_largest(arr)
    k=0
    sum=0
    for i in range(len(arr)):
        if arr[i]==larg2:
            k=i
    for i in range(k,len(arr)):
        if arr[i]<larg2:
            dif=larg2-arr[i]
            sum+=dif
    print(sum)

# arr=[3,0,0,2,0,4]
# arr=[7,4,0,9]
# arr=[6,9,9]
arr=[3,5,7,2,6,4,9]
trappingWater(arr)

