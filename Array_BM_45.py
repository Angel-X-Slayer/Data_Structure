def find_pair_close_sum(arr,x):
    ## Process1......................

    # for i in range(len(arr)-1,-1,-1):
    #     # print(arr[i])
    #     if arr[i]<x:
    #         temp=arr[i]
    # diff=x-temp
    # for i in range(len(arr)):
    #     diff1=diff-arr[i]
    #     if diff1<diff:
    #         temp1=arr[i]
    # print(temp,temp1)

    ## End of Precess1................

    ##..........****************.............##

    ## Precoess2......................
    # temp1=temp2=0
    # i=0
    # j=len(arr)-1
    # dif=arr[0]
    # while i<j:
        
    #     if  abs(arr[i]+arr[j]-x)<dif:
    #         dif=abs(arr[i]+arr[j]-x)
    #         temp1=arr[i]
    #         temp2=arr[j]
    #     i+=1
    #     j-=1
    # print(temp1,temp2)

    ## End of Precoess2

    ##........................*****************..................##

    ## Process3.............

    res_l,res_r=0,0
    l=0
    r=len(arr)-1
    dif=1000000000000000000
    while l<r:
        if abs(arr[l]+arr[r]-x)<dif:
            res_l=l
            res_r=r
            dif=abs(arr[l]+arr[r]-x)
        if arr[l]+arr[r]>x:
            r-=1
        else:
            l+=1
    print(arr[res_l],arr[res_r])

## End of Process 3

##......................*******************....................##























# arr=[10, 22, 28, 29, 30, 40]
# x=54
arr=[11,12 ,13, 15, 19, 22, 23, 24, 24, 25, 31, 33, 38, 39, 49, 49, 51, 51, 52, 60, 60, 61, 63, 64, 65, 66, 67, 67, 68, 69, 71, 72, 76, 80, 80, 83, 87, 90, 94, 96, 97, 99, 99]
x=431

find_pair_close_sum(arr,x)