# def magic_squre(n):
#     # arr=[]
#     # # n=int(input("enter the number of rows and columns :"))
#     # for i in range(n):
#     #     brr=[]
#     #     for j in range(n):
#     #         item=int(input("enter the number :"))
#     #         brr.append(item)
#     #     arr.append(brr)
#     # print("the matrix is :")
#     # for i in range(n):
#     #     for j in range(n):
#     #         print(arr[i][j],end=" ")
#     #     print()

#     arr=[[0 for x in range(n)]for y in range(n)]
#     i=int(n/2)
#     j=n-1
#     num=1
#     # print(i,j)
#     # print(magic[i][j])
#     n2=n*n
#     for num in range(1,n2+1):
#         if arr[i][j]!=0:
#             j-=2
#             i+=1
#             arr[i][j]=num
#         if i==-1 and j==n:
#             i=0
#             j=n-2
#             arr[i][j]=num
#         if i==-1:
#             i=n-1
#             arr[i][j]=num
#         elif j==n:
#             j=0
#             arr[i][j]=num
#         else:
#             arr[i][j]=num
#             i-=1
#             j+=2
#     # while num<=(n*n):
#     #     if magic[i][j]==0:

#     #         if i==-1:
#     #             i=n-1
#     #         elif j==n:
#     #             j=0
#     #         elif (i==-1 and j==n):
#     #             i=0
#     #             j=n-2
#     #         else:
#     #             magic[i][j]=num
#     #             i-=1
#     #             j+=1
#     #         num+=1
#     #     else:
#     #         i+=1
#     #         j-=2
#     #         magic[i][j]=num
#     #         num+=1
            


#     for i in range(n):
#         for j in range(n):
#             print(arr[i][j],end=" ")
#         print()




# n=int(input("enter the number of rows and columns :"))
# magic_squre(n)







# Python program to generate
# odd sized magic squares
# A function to generate odd
# sized magic squares

from typing import Mapping, MappingView


def generateSquare(n):
	magicSquare = [[0 for x in range(n)] ## this is how we can initialize 
				for y in range(n)] ## a mXn matrix with 0 as a value
	i = n // 2
	j = n - 1
	num = 1
	while num <= (n * n):
		if i == -1 and j == n: # 3rd condition
			j = n - 2
			i = 0
		else:
			if j == n:
				j = 0
			elif i < 0:
				i = n - 1
		if magicSquare[i][j]!=0: # 2nd condition
			j = j - 2
			i = i + 1
			continue
		magicSquare[int(i)][int(j)] = num
		num = num + 1

		j = j + 1
		i = i - 1 # 1st conditio
	for i in range(n):
		for j in range(n):
			print(magicSquare[i][j],end=" ")
		print()

	

# Driver Code


# Works only when n is odd
n =3


generateSquare(n)

# This code is contributed
# by Harshit Agrawal


# magic=[[ for x in range(7)]for y in range(7)]
# for i in range(7):
#     for j in range(7):
#         print(magic[i][j],end=" ")
#     print()


 ## A hard looking problem with a easy solution, just find the solution.........