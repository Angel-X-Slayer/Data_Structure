# class StackNode:
#     def __init__(self,size):
#         self.arr=[]*size
#         self.capacity=size
#         self.top=-1
#     def push(self,item):
#         if self.top==self.capacity-2:
#             print("Stack Overflow!! Calling exit()…")
#         else:
#             self.top+=1
#             self.arr[self.top]=item
    
#     def operation(self,expr):
#         x=1
#         for i in expr:
#             if i in ["(","{","["]:
#                 self.push(i)
#             else:
#                 if not self.arr:
#                     return False
#                 cur_i=self.arr.pop()
#                 if cur_i=="(":
#                     if i!=")":
#                         print("not balanced")
#                         x=0
#                         break
#                 if cur_i=="{":
#                     if i!="}":
#                         print("not balanced")
#                         x=0
#                         break
#                 if cur_i=="[":
#                     if i!="]":
#                         print("not balanced")
#                         x=0
#                         break
#         if x==0:
#             pass
#         else:
#             print("balanced")

# if __name__ == "__main__":
#     expr = "[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]"
#     n=len(expr)
#     stackk=StackNode(n)
#     stackk.operation(expr)




 
#     # Function call
#     if areBracketsBalanced(expr):
#         print("Balanced")
#     else:
#         print("Not Balanced")

class Stack_Node:
    def __init__(self,size):
        self.size=size
        self.arr=[]*size
        self.top=-1
        

















