# # def findh(arr,n,k):
# #     mid=int((0+(n-1))/2)
# #     h_max=0
# #     arr1=sorted(arr)
# #     i=0
# #     while i<mid:
# #         arr1[i]+=k
# #         i+=1
# #     while i<n:
# #         arr1[i]-=k
# #         i+=1
# #     l,r=0,(n-1)
# #     while l<=mid and r>mid:
# #         h=arr1[r]-arr1[l]
# #         if h>h_max:
# #             h_max=h
# #             l+=1
# #             r-=1
# #     print (h_max)
# def findh(arr, n, k):
#     arr1=sorted(arr)
#     mid=int((0+(n-1))/2)
#     l=0
#     r=n-1
#     h=0
#     hmax=0
#     while l<=mid and r>mid:
#         arr1[l]+=k
#         l+=1
#         if  arr1[r]<k:
#             arr1[r]+=k
#         else:
#             arr1[r]-=k
#         r-=1
#     l=0
#     r=n-1
#     # print(arr1)
#     # while l<=mid and r>mid:
#     #     if arr1[l]>arr1[r]:
#     #         h=arr1[l]-arr[r]
#     #     else:
#     #         h=arr1[r]-arr1[l]
#     #     if h>hmax:
#     #         hmax=h
#     #     l+=1
#     #     r-=1
#     # print (hmax)
#     min=arr1[0]
#     max=arr1[n-1]
#     # for i in range(1,n):
#     #     if arr[i]<=min:
#     #         min=arr1[i]
#     #         i+=1
#     #     elif arr[i]>=max:
#     #         max=arr1[i]
#     #         i+=1 
#     for i in range(1,n,1):
#         if arr1[i]<=min:
#             min=arr1[i] 
#         elif arr1[i]>=max:
#             max=arr1[i]  
#     h=max-min
#     # print(h)
#     print(min,max)

# if __name__=="__main__":
#     arr=[]
#     n=int(input("enter the lenth of the array: "))
#     k=int(input("entr the value of k:"))
#     for i in range(n):
#         num=int(input("enter the number: "))
#         arr.append(num)
#     findh(arr,n,k)




def getMinDiff(arr, n, k):
        arr.sort() ## here we have to use quick sort for better result
        ans=arr[n-1]-arr[0] 
        small,big=0,0
        
        for i in range(1,n):
          small=min(arr[0]+k,arr[i]-k) 
          big=max(arr[i-1]+k,arr[n-1]-k) 
          ans=min(ans,big-small)
            
            
        print (small,big)
        return ans
if __name__=="__main__":

  #arr=[2,6,3,4,7,2,10,3,2,1]
  #k=5
  arr=[]
  n=int(input("enter the lenth of the array"))
  k=int(input("enter the target:"))
  for i in range (n):
    num=int(input("enter the numbers"))
    arr.append(num)

  print(getMinDiff(arr,len(arr),k))
