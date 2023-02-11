## O(N2) tym complexity
# def biggest_sum(arr):
#     max_sum=0
#     for i in range(len(arr)):
#         sum=0
#         for j in range(i,len(arr)):
#             sum+=arr[j]
#             if sum>max_sum:
#                 max_sum=sum
#     print(max_sum) 

##O(N) tym complexity__ # Kadane's Algorithem
def biggest_sum(arr):
    i=0
    max_sum=arr[0]
    sum=0
    mi=min(arr)
    while i<len(arr):
        sum+=arr[i]
        if max_sum<sum:
            max_sum=sum
        if sum<mi or sum<0:
            sum=0
        i+=1

    print(max_sum)

# in this Kadane's algorithem take i=0 to itreate through the array.
# take 'max_sum' to store the max sum and initialize it to the first number of the array.
# take 'sum' to stote the current sum.
# take a variable mi to store the minimum element in the array.
# first itrate through the array and ad  the elements in the 'sum' variable.
# then check if 'max_sun' is smaller than 'sum' or not . if so then assign the 'sum' to 'max_sum' 
# then checkif the sum is less than mi or not.
#if sum is less than mi that means the produced sum less than then minimum element and we should change the sum to 0.
# the upper line is only done if an negetive number array is given.
# after termination of the loop print the 'max_sum'





if __name__=="__main__":
    n=int(input("enter the lenth of the array :"))
    arr=[]
    for i in range(n):
        num=int(input("enter the number :"))
        arr.append(num)
    biggest_sum(arr)
    # print(arr)
