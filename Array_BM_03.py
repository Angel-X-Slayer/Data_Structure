def reverse_an_array(arr):
    # i=0       ##1st method without in-built function
    # j=len(arr)-1
    # while(i<j):
    #     temp=arr[i]
    #     arr[i]=arr[j]
    #     arr[j]=temp
    #     i+=1
    #     j-=1




    arr.reverse()  ##2nd method with in-built function
    return arr

if __name__=="__main__":
    n=int(input("enter the limit:"))
    arr=[]

    for i in range(n):
        num=int(input("enter the number:"))
        arr.append(num)    
    arr=reverse_an_array(arr)
    print("the reversed array is :",arr)
