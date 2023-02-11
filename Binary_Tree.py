from platform import node

from numpy import true_divide
from collections import deque as dq


class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def insert(self,data):
        if self.data:
            if data<=self.data:
                if self.left ==None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right==None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)

        # else:
        #     self.data=Node(data)
    
    def INprntBT(self):        ##___D_F_S___##
        if self.left:
            self.left.INprntBT()
        print(self.data,end=" ")
        if self.right:
            self.right.INprntBT()
    
    def PreprntBT(self):       ##___D_F_S___##
        print(self.data,end=" ")
        if self.left:
            self.left.PreprntBT()
        if self.right:
            self.right.PreprntBT()
    
    def PstprntBT(self):      ##___D_F_S___##
        if self.left:
            self.left.PstprntBT()
        if self.right:
            self.right.PstprntBT()
        print(self.data,end=" ")
    
    def delete(self,data,root):
        if data==self.data:
            i=root.deletedeep()
            self.data=i.data
        elif data<self.data:
            self.left.delete(data,root)
        else:
            self.right.delete(data,root)
    def deletedeep(self):
        m=self
        while self.right!=None:
            self=self.right
        while m.right.data!=self.data:
            m=m.right
        m.right=None
        return (self)
    def Search(self,data):
        if data==self.data:
            print(1)
        elif data<self.data:
            self.left.Search(data)
        elif data>self.data:
            self.right.Search(data)
        else:
            print(0)
    
    def Prnt_lvl_order(self):    ##___B_F_S___##
        if self==None:
            return
        q=[]
        q.append(self)
        while (len(q)>0):
            print(q[0].data, end=" ")
            node=q.pop(0)
            if node.left!=None:
                q.append(node.left)
            if node.right!=None:
                q.append(node.right)
    def INord_no_rec(self):
        current=self
        s=[]
        while True:
            if current!=None:
                s.append(current)
                current=current.left
            elif (s):
                current=s.pop()
                print(current.data,end=" ")
                current=current.right

            else:
                break
    def Preord_no_rec(self):
        current=self
        s=[]
        s.append(current)
        while len(s)>0:
            node=s.pop()
            print(node.data,end=" ")
            if node.right!=None:
                s.append(node.right)
            if node.left!=None:
                s.append(node.left)
    
    
    def check_if_mirroi(self,root1):
        if self==None and root1==None:
            return(0)
        elif self!=None and root1!=None:
            if self.data==root1.data:
                (Node.check_if_mirroi(self.left,root1.right)and (self.left,root1.right))
        else:
            return(1)

    def sum_of_left_subtree(self):
        if self==None:
            return 0
        if self.left==None and self.right==None:
            return self.data
        else:
            leftsum=Node.sum_of_left_subtree(self.left)
            rightsum=Node.sum_of_left_subtree(self.right)
            self.data+=leftsum
            return(self.data+rightsum)


    def nthinorder(self,n,k):
        if self.left:
            self.left.nthinorder(n,k)
        k.append(self.data)
        if self.right:
            self.right.nthinorder(n,k)
        return(k)


    def nthpostorder(self,n,k):
        if self.left:
            self.left.nthpostorder(n,k)
        if self.right:
            self.right.nthpostorder(n,k)
        k.append(self.data)
        return k


    def lvl_ordr_line_by_line(self):
        if self==None:
            return
        queue=dq()
        queue.append(self)
        queue.append(None)
        while len(queue)>1:
            curr=queue.popleft()
            if curr==None:
                queue.append(None)
                print()
            else:
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                print(curr.data,end=" ")
    

    def inverted_binary_tree(self):
        if self.left==None and self.right==None:
            return
        else:
            Node.inverted_binary_tree(self.left)
            Node.inverted_binary_tree(self.right)
            temp=self.left
            self.left=self.right
            self.right=temp


    def find_height(self):
        k,r=0,0
        temp=self
        while self!=None:
            self=self.left
            k+=1
        while temp!=None:
            temp=temp.right
            r+=1
        if k>r:
            # print(k)
            return(k)  ##used only for reverse_lvl_order
        else:
            # print(r)
            return(r)  ##used only for reverse_lvl_order

    # def reverse_lvl_order(self):
    #     h=self.find_height()
    #     for i in range(h,0,-1):
    def longest_path(self):
        if (self == None):
            return ([])
 
    # Recursive call on root.right
        rightvect = Node.longest_path(self.right)

    # Recursive call on root.left
        leftvect = Node.longest_path(self.left)
 
    # Compare the size of the two vectors
    # and insert current node accordingly
        if (len(leftvect) > len(rightvect)):
            leftvect.append(self.data)
        else:
            rightvect.append(self.data)
 
    # Return the appropriate vector
        if len(leftvect) > len(rightvect):
            return(leftvect)
 
        return(rightvect)



        

            


    
    



    # def morris_traversal(self):  ## no stack no recursion used for traversal


## INPUT THE DATA


# k=[]     ## type 1 input method
# n=int(input("enter how many number you want to insert : "))
# for i in range(n):
#     a=int(input("enter the number :"))
#     k.append(a)
# root=Node(k[0])
# for i in range(1, len(k)):
#     root.insert(k[i])



a=[27,14,35,10,19,31,42]
# a=[1,2,3,4,5,6]  ##type 2 input method
root=Node(a[0])
for i in range(1, len(a)):
    root.insert(a[i])



# root = Node(27)     ##type 3 input metgod
# root.insert(14)
# root.insert(35)
# root.insert(10)
# root.insert(19)
# root.insert(31)
# root.insert(42)



# root = Node(1)      ##ttype 4 of taking input
# root.left =Node(2)
# root.right =Node(3)
# root.left.left =Node(4)
# root.left.right =Node(5)
# root.right.right =Node(6)



# ACTUAL OPERATION


# root.Prnt_lvl_order()


# root.INord_no_rec()


# root.Preord_no_rec()


# root.INprntBT()


# root.PreprntBT()


# root.PstprntBT()


# root.INprntBT()
# print()
# root.deletedeep()
# print()
# root.INprntBT()


# root.delete(27,root)
# print("\n")
# print()
# root.PreprntBT()


# root.Search(42)


# root.sum_of_left_subtree()
# print()
# root.INprntBT()


# n=4
# k=[]
# j=root.nthinorder(n,k)
# print(j[n-1])

# root.Prnt_lvl_order()


# s=root.check_if_mirroi(root)
# if s==0:
#     print("mirror tree")
# else:
#     print("not mirror tree")


# root.lvl_ordr_line_by_line()



# print("the oruginal inorder tree is :",end=" ")
# root.INprntBT()
# print()
# print("the inverted inorder tree is :",end=" ")
# root.inverted_binary_tree()
# root.INprntBT()



# n=4
# k=[]
# j=root.nthpostorder(n,k)
# print(j[n-1])



# root.find_height()


c=root.longest_path()
print(c)



















































































































































# class Node:
#    def __init__(self, data):
#       self.left = None
#       self.right = None
#       self.data = data

#    def insert(self, data):
# # Compare the new value with the parent node
#       if self.data:
#         if data < self.data:
#             if self.left is None:
#                self.left = Node(data)
#             else:
#                self.left.insert(data)
#         elif data > self.data:
#             if self.right is None:
#                 self.right = Node(data)
#             else:
#                 self.right.insert(data)
#       else:
#          self.data = data

# # Print the tree
#    def PrintTree(self):
#       if self.left:
#          self.left.PrintTree()
#       print( self.data)
#       print( )
#       if self.right:
#          self.right.PrintTree()

# # Use the insert method to add nodes
# root = Node(12)
# root.insert(6)
# root.insert(14)
# root.insert(3)
# root.PrintTree()
# class Node:
#    def __init__(self, data):
#       self.left = None
#       self.right = None
#       self.data = data
# # Insert Node
#    def insert(self, data):
#       if self.data:
#          if data < self.data:
#             if self.left is None:
#                self.left = Node(data)
#             else:
#                self.left.insert(data)
#          else data > self.data:
#             if self.right is None:
#                self.right = Node(data)
#             else:
#                self.right.insert(data)
#       else:
#          self.data = data
# # Print the Tree
#    def PrintTree(self):
#       if self.left:
#          self.left.PrintTree()
#       print( self.data),
#       if self.right:
#          self.right.PrintTree()
# # Inorder traversal
# # Left -> Root -> Right
#    def inorderTraversal(self, root):
#       res = []
#       if root:
#          res = self.inorderTraversal(root.left)
#          res.append(root.data)
#          res = res + self.inorderTraversal(root.right)
#       return res
# root = Node(27)
# root.insert(14)
# root.insert(35)
# root.insert(10)
# root.insert(19)
# root.insert(31)
# root.insert(42)
# print(root.inorderTraversal(root))  




































# # A recursive Python program to print REVERSE level order traversal

# # A binary tree node
# class Node:

#     # Constructor to create a new node
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# # Function to print reverse level order traversal
# def reverseLevelOrder(root):
#     h = height(root)
#     # for i in reversed(range(0, h+1)):
#     for i in range(h,0,-1):
#         printGivenLevel(root,i)

# # Print nodes at a given level
# def printGivenLevel(root, level):

#     if root is None:
#         return
#     if level ==1 :
#         print (root.data,end=" ")

#     elif level>1:
#         printGivenLevel(root.left, level-1)
#         printGivenLevel(root.right, level-1)

# # Compute the height of a tree-- the number of
# # nodes along the longest path from the root node
# # down to the farthest leaf node
# def height(node):
#     k,r=0,0
#     if node is None:
#         return 0
#     temp=node
#     while node!=None:
#         node=node.left
#         k+=1
#     while temp!=None:
#         temp=temp.right
#         r+=1
#     if k>r:
#         return(k)
#     else:
#         return(r)

# # Driver program to test above function
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)

# print ("Level Order traversal of binary tree is")
# reverseLevelOrder(root)

# # This code is contributed by Nikhil Kumar Singh(nickzuck_007)



# class Node:
#     def __init__(self,data):
#         self.left=None
#         self.right=None
#         self.data=data
#     def insert(self,data):
#         if self.data:
#             if data<=self.data:
#                 if self.left ==None:
#                     self.left=Node(data)
#                 else:
#                     self.left.insert(data)
#             elif data>self.data:
#                 if self.right==None:
#                     self.right=Node(data)
#                 else:
#                     self.right.insert(data)
#     def longest_path(self):
#         if (self == None):
#             return []
 
#     # Recursive call on root.right
#         rightvect = Node.longest_path(self.right)

#     # Recursive call on root.left
#         leftvect = Node.longest_path(self.left)
 
#     # Compare the size of the two vectors
#     # and insert current node accordingly
#         if (len(leftvect) > len(rightvect)):
#             leftvect.append(self.data)
#         else:
#             rightvect.append(self.data)
 
#     # Return the appropriate vector
#         if len(leftvect) > len(rightvect):
#             print(leftvect)
 
#         print(rightvect)
# k=[]     ## type 1 input method
# n=int(input("enter how many number you want to insert : "))
# for i in range(n):
#     a=int(input("enter the number :"))
#     k.append(a)
# root=Node(k[0])
# for i in range(1, len(k)):
#     root.insert(k[i])
# root.longest_path()