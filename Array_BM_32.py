def findtriplenumber(arr,n,tar):
    # c,i,sum=0,0,0
    # while i<n:
    #     sum+=arr[i]
    #     if sum==tar:
    #         c+=1
    #     elif sum>tar:
    #         sum-=arr[i]
    #         i+=1
    #     else:
    #         i+=1
    # print(sum)
    # return(c)
    # i,c=0,0
    # arr=sorted(arr)
    # while i<n-2:
    #     j=i+1
    #     k=n-1
    #     while j<k:
    #         if arr[j]+arr[k]==tar-arr[i]:
    #             c+=1
    #         elif arr[j]+arr[k]>tar-arr[i]:
    #             k-=1
    #         else:
    #             j+=1
    # return(c)
    i=0
    arr=sorted(arr)
    while i<n-2:
        j=i+1
        k=n-1
        while j<k:
            if arr[j]+arr[k]==tar-arr[i]:
                print(arr[i],arr[j],arr[k])
                return True
                break
                    
            elif arr[j]+arr[k]>tar-arr[i]:
                k-=1
            else:
                j+=1
    return(False)
    # print(arr)

if __name__=="__main__":
    # arr=[1,4,45,6,10,8]
    arr=[1,4,45,6,10,8]
    tar=13
    n=6
    l=findtriplenumber(arr,n,tar)
    if l==True:
        pass
    else:
        print(-1)
