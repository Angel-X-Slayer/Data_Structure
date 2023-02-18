def binaryofnum(i):
    return(bin(i).replace("0b",""))
def onesinbin(j):
    one_count=0
    j=str(j)
    for i in j:
        if i=="1":
            one_count+=1
    return(one_count)          
def cardinalitySort(nums):
    arr=[]*100
    brr=[]*100
    for i in range(len(nums)):
        k= binaryofnum(nums[i])
        # arr[nums[i]]=k
        arr.insert(i,k)
    for i in range(len(arr)):
        l=onesinbin(arr[i])
        # brr[nums[i]]=l
        brr.insert(i,l)
    zipped_pairs = zip(brr, nums)
 
    z = [x for _, x in sorted(zipped_pairs)]
     
    print(arr)
    print(brr)
    print(z)

# nums=[1,2,3,4]
nums=[5,31,15,7,3,2]
# p=sorted(nums)
print(nums)
cardinalitySort(nums)