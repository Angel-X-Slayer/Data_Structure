# def binarysearch(key,arr,l,r):
#     if l<=r:
#         mid=(l+r)//2
#         if arr[mid]==key:

#             return(1,mid)

#         if arr[mid]<key:
#             return(binarysearch(key,arr,mid+1,r))
#         else:
#             return(binarysearch(key,arr,l,mid-1))
#     else:
#         return(-1,-1)


# def max_sum_path(a1,a2):
#     l1=len(a1)
#     l2=len(a2)
#     # print(a1,a2,l1,l2)
#     sum1=0
#     sum2=0
#     if l1>=l2:
#         for i in range(l2):
#             nas,idx=binarysearch(a2[i],a1,0,l1-1)
        
#             if nas==1:
#                 k=i
#                 k2=idx
#                 print(k)
#                 print(k2)
#                 break
#             else:
#                 print("no common element in the arrays")
#                 break
#         if nas==1:
#             for i in range(k+1):
#                 sum1=sum1+a2[i]
#             print(sum1)
#             for j in range(k2+1):
#                 sum2=sum2+a1[j]
#             print(sum2)
#             if sum1>sum2:
#                 for i in range(k2,l1):
#                     sum1=sum1+a1[i]
#                 print(sum1)

#             else:
#                 for i in range(k,l2):
#                     sum2=sum2+a2[i]
#                 print(sum2)
#     else:
#         for i in range(l1):
#             nas,idx=binarysearch(a1[i],a2,0,l2-1)
#             if nas==1:
#                 k=i
#                 k2=idx
#                 break
#             else:
#                 print("no common element in the array,yui")
#                 break
#         if nas==1:
#             for i in range(k+1):
#                 sum1=sum1+a1[i]
#             for j in range(k2+1):
#                 sum2=sum2+a1[j]
#             if sum1>sum2:
#                 for i in range(k2,l1):
#                     sum1=sum1+a1[i]
#                     print(sum1)

#             else:
#                 for i in range(k2,l2):
#                     sum2=sum2+a2[i]
#                     print(sum2)


    
# def max_sum_path(a1,a2):
#     l1=len(a1)
#     l2=len(a2)
#     sum1=0
#     sum2=0
#     k2,k1=0,0
#     a=[]
#     if l1>=l2:
#         ## we should take each and every a2 element and find its pair in a1 array
#         for i in range(l2):
#             y_n,idx=binarysearch(a2[i],a1,0,l1-1)## here l=0 & r=(lenth of a1)-1
#             print(y_n)
#             a.append(y_n)
#             ## i will give the index of the element at a2; basically a2 index
#             ## y_n will indicate if the element in a2 is found in array a1 or not
#             ## idx will give the index of a2 array element in array a1; basically a1 index
#             if y_n==1:
#                 k2=i ## k2 is besically a2 index
#                 k1=idx ## k1 is basically a1index
#                 break
#             else:
#                 print("tehere is not such element in the array")
#                 break
#         if y_n==1:
#             for j in range(k2+1):
#                 sum2=sum2+a2[j]
#             for j in range(k1+1):
#                 sum1=sum1+a1[j]
#             if sum1>sum2:
#                 for j in range(k2+1,l2):
#                     sum1=sum1+a2[j]
#                     print(sum1)
#             else:
#                 for j in range(k1+1,l1):
#                     sum2=sum2+a1[j]
#                     print(sum2)








# a1=[2,3,7,10,12]
# a2=[1,5,7,8]
# # a2=[11,15,17,19,22,24]
# # a1=[1,2,3]
# # a2 = [3,4,5]
# max_sum_path(a1,a2)

# Python program to find maximum sum path

# This function returns the sum of elements on maximum path from
# beginning to end


def maxPathSum(ar1, ar2, m, n):

	# initialize indexes for ar1[] and ar2[]
	i, j = 0, 0

	# Initialize result and current sum through ar1[] and ar2[]
	result, sum1, sum2 = 0, 0, 0

	# Below 3 loops are similar to merge in merge sort
	while (i < m and j < n):

		# Add elements of ar1[] to sum1
		if ar1[i] < ar2[j]:
			sum1 += ar1[i]
			i += 1

		# Add elements of ar2[] to sum2
		elif ar1[i] > ar2[j]:
			sum2 += ar2[j]
			j += 1

		else: # we reached a common point

			# Take the maximum of two sums and add to result
			result += max(sum1, sum2) +ar1[i]
			#update sum1 and sum2 to be considered fresh for next elements
			sum1 = 0
			sum2 = 0
			#update i and j to move to next element in each array
			i +=1
			j +=1

		

	# Add remaining elements of ar1[]
	while i < m:
		sum1 += ar1[i]
		i += 1
	# Add remaining elements of b[]
	while j < n:
		sum2 += ar2[j]
		j += 1

	# Add maximum of two sums of remaining elements
	result += max(sum1, sum2)

	return result


# Driver code
ar1 = [2, 3, 7, 10, 12, 15, 30, 34]
ar2 = [1, 5, 7, 8, 10, 15, 16, 19]
m = len(ar1)
n = len(ar2)

# Function call
print ("Maximum sum path is", maxPathSum(ar1, ar2, m, n))

# This code is contributed by __Devesh Agrawal__
