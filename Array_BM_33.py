def segregation(arr,n):
    j=0
    for i in range(n):
        if arr[i]<0:
            arr[i],arr[j]=arr[j],arr[i]     
            j+=1
    # print(arr)
    # print(j)
    return(arr,j)




def findmissing(arr,n):
    c=1
    arr,pos=segregation(arr,n)
    if max(arr)<0:
        print(1)
    else:
    # print(arr)
    # print(pos)
    
        for i in range(pos,n):
            if arr[i]>n:
                pass
            else:
                arr[i]=arr[i]*(-1)
    # print(arr)
    # print(i)
        for i in range(pos,n):
            if arr[i]>0:
                i=i-pos
                break
            else:
                c+=1
    # print(c)
    # print(i)
   
        if c==n+1:
            print(c)
        else:
            print(i)

# arr=[28,7,-36,21,-21,-50,9,-32]
arr=[1,2,3,4,5]
# arr=[-1,-2,-3,-4,-5,-6,-7,-8]
findmissing(arr,n=5)
# segregation(arr,n=8)




