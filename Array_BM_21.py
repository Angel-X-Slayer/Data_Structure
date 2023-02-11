def check_zero(arr):
    n_sum=0
    s=[]
    for i in range(len(arr)):
        n_sum+=arr[i]
        if n_sum==0 or n_sum in s:
            return ("yes")
        s.append(n_sum) 
    return ("no")

if __name__=="__main__":
    n=int(input("enter the lenthe of the array:"))
    arr=[]
    for i in range(n):
        num=int(input("enter the number"))
        arr.append(num)
    k=check_zero(arr)
    print(k)
        
# here to check if there is any sub array with sum=0, u have to take a variable n_sum=0.
# assign a list name s, and append the prefix sum iin this array.
# we can check this cond by two options, first one is by checking if the sum is 0 or not or the other way is to check,
# seceondly,if there is any repeatating element is the array or not. if there is any repeatating element,that means there is
# a legit subarray with sum=0