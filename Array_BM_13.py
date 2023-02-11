def selection_sort(arr):
    i=0
    for i in range(len(arr)):
         mi=i
         for j in range(i+1,len(arr)):
             if arr[mi]>arr[j]:
                 mi=j
         arr[mi],arr[i]=arr[i],arr[mi]
    return(arr)
def find_pair(arr,k):
    # l=len(arr)
    # i=0
    # c=0
    # j=0
    # while i<l and j<l:
    #     j=i+1
    #     if arr[i]+arr[j]==k:
    #         c+=1
    #         j+=1
    #     j=i+1
    # print(c)
    arr=selection_sort(arr)
    # print(arr)
    i=0
    j=len(arr)-1
    c=0
    while i<j:
        if arr[i]+arr[j]>k and i!=j:
            j-=1
        if arr[i]+arr[j]<k and i!=j:
            i+=1
        if arr[i]+arr[j]==k and i!=j:
            print(arr[i],arr[j])
            i+=1
            # j-=1
            c+=1
    print(c)
if __name__=="__main__":
    arr=[]
    k=int(input("enter the target:"))
    n=int(input("enter the lenth of the array:"))
    for i in range(n):
        num=int(input("enter the number:"))
        arr.append(num)
    find_pair(arr,k)