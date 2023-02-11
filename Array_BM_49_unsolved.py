def coin_change(arr,sum,n):
    t=[[-1 for i in range(sum+1)]for j in range(n+1)]
    # print(t)
    
    for i in range(n+1):
        for j in range(sum+1):
            if j==0:
                t[i][j]=1
            elif i==0:
                t[i][j]=0
    # print(t)
    for i in range(n+1):
        for j in range(sum+1):
            if arr[i-1]<=j:
                t[i][j]=t[i][j-arr[i-1]]+t[i-1][j]
            else:
                t[i][j]=t[i-1][j]
    # for i in range(n+1):
    #     for j in range(sum+1):
    #         print(t[i][j],end=" ")
    #     print()
    return(t[n][sum])


arr=[1,2,3]
sum=4
n=3
print(coin_change(arr,sum,n))
    