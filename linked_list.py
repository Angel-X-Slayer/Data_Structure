'''                                 IMPORTANT INFORMATION
if you return self.head from a Linked_list class function to the main function and recieve that self.head into a variable,
then to perform any opration on that perticular variable you have define functions outside of the class Linked_list, 
otherwise if will give you an error like "Node 'a' doesn't have head attribute.
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class Linked_list:
    def __init__(self):
        self.head = None

    def delete_from_front(self):
        if self.head == None:
            print("No node is there to delete")
        else:
            self.head = self.head.ref

    def delete_from_end(self):
        if self.head == None:
            print("No node to delete")
        else:
            n = self.head
            while n.ref != None:
                n = n.ref
            n.ref = None

    def adding_in_front(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.ref = self.head
            self.head = new_node

    def adding_at_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.ref != None:
                n = n.ref
            n.ref = new_node

    def adding_after_specific_node(self, data, target):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n != None:
                if n.data == target:
                    new_node.ref = n.ref
                    n.ref = new_node
                    break
                else:
                    n = n.ref
            if n == None:
                # print("no target found !!!")
                return (-1)
            else:
                return (self.head)

    def adding_before_specific_node(self, data, target):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            # while n.ref.ref!=None:
            #     if n.ref.data==target:
            #         new_node.ref=n.ref
            #         n.ref=new_node
            #         break
            #     else:
            #         n=n.ref
            # if n.ref==None:
            #     # print("no target found !!!")
            #     return(-1)
            # else:
            #     return(self.head)
            while n.ref.ref != None:
                if n.ref.data == target:
                    new_node.ref = n.ref
                    n.ref = new_node
                    ko = -1
                    break
                else:
                    n = n.ref

            if ko == -1:
                return self.head
            else:
                return (None)

    def traversal(self):
        if self.head == None:
            print("empty linked List")
        else:
            n = self.head
            while n != None:
                print(n.data, end=" -> ")
                n = n.ref

    def reversal(self):
        prev = None
        n = self.head
        while n != None:
            next = n.ref
            n.ref = prev
            prev = n
            n = next
        self.head = prev

    def rotate_a_linked_list(self, n):    # locate n+1th node, make it self.head
        tenp = self.head                  # locate nth node, make nth node.ref=None
        tenp1 = self.head                 # locate to the last node of the original linked list
        var = 0                           # assign the original self.head to that node.ref,
        var1 = 0                          # in this case that was tenp1

        while self.head != None and var < 4:
            self.head = self.head.ref
            var += 1
        while var1 < 3 and tenp != None:
            tenp = tenp.ref
            var1 += 1
        tenp.ref = None
        k = self.head
        while k.ref != None:
            k = k.ref
        k.ref = tenp1

        # type1 of doing this problem
    def singly_to_circular(self):  # store the head in tenp1 variable
        # n = 0                                                              ## locate to n+1th node, make that self.head
        # var = 0                                                            ## locate to the actual end of the linked list
        # tenp1 = self.head                                                  ## attach the original head to the original tail

        # while self.head != None and var < n:
        #     self.head = self.head.ref
        #     var += 1

        # k = self.head

        # while k.ref != None:
        #     k = k.ref
        # k.ref = tenp1

        n = self.head  # type2 of solving this problem
        while n.ref != None:
            n = n.ref
        n.ref = self.head

    def travarsal_circular(self, target):
        if self.head == None:
            print("empty linked List")
        else:
            k = 0
            n = self.head
            while n != None and k < target:
                print(n.data, end=" -> ")
                n = n.ref
                k += 1

    def marge_two_linked_list(self, ll1):
        n = self.head
        while n != None:
            n = n.ref
        n.ref = ll1

    def cut_linked_list_into_specific_portion(self, target):
        n = self.head
        count = 0
        while n != None and count < target:
            n = n.ref
        k = n
        return (self.head, k)

    def reverse_a_linkedl_list_in_groups_of_given_size(self):
        pass
    # def marge_two_sorted_linked_list()

    def make_loop(self, k):
        temp = self.head
        count = 1
        while (count < k):
            temp = temp.ref
            count += 1
        kth_node = temp

        temp = self.head
        while (temp.ref):
            temp = temp.ref
        temp.ref = kth_node


# # Adding node in front of the linked list
# arr = list(map(int, input("enter array elements : ").split(' ')))
# obj = Linked_list()
# for i in arr:
#     obj.adding_in_front(i)
# obj.traversal()  # end of the input

# # Adding node at the end of the linked list
# arr = list(map(int, input("enter array elements : ").split(' ')))
# obj = Linked_list()
# for i in arr:
#     obj.adding_at_end(i)
# obj.traversal()  # end of the input

# # Adding node after a specific node of the
# arr = list(map(int, input("enter array elements : ").split(' ')))
# target = int(input("enter the target node :"))  # linked list
# value = int(input("entre value to insert :"))
# obj = Linked_list()
# for i in arr:
#     obj.adding_in_front(i)
# k = obj.adding_after_specific_node(value, target)
# if k != -1:
#     obj.traversal()
# else:
#     print("No target found!!!")  # end of the input

# arr=list(map(int,input("enter array elements : ").split(' '))) ## Adding node before a specific node of the
# target=int(input("enter the target node :"))                   ## linked list
# value=int(input("entre value to insert :"))
# obj=Linked_list()
# for i in arr:
#     obj.adding_at_end(i)
# k=obj.adding_before_specific_node(value,target)
# if k!=None:
#     obj.traversal()
# else:
#     print("No target found!!!")

# arr=list(map(int,input("enter array elements : ").split(' ')))  ## Deleting a node from the front
# obj=Linked_list()
# for i in arr:
#     obj.adding_at_end(i)
# obj.delete_from_front()
# obj.delete_from_front()
# obj.traversal()
# print("NULL")


# arr=list(map(int,input("enter array elements : ").split(' ')))  ## Deleting a node from the front
# obj=Linked_list()
# for i in arr:
#     obj.adding_at_end(i)
# obj.delete_from_end()
# # obj.delete_from_front()
# obj.traversal()
# print("NULL")

# arr = list(map(int, input("enter array elements : ").split(' ')))  ##Reversal of a linked list
# obj = Linked_list()
# for i in arr:
#     obj.adding_at_end(i)
# obj.traversal()
# obj.reversal()
# print()
# obj.traversal()


# arr = list(map(int, input("enter array elements : ").split(' ')))     ## Rotate a Linked List from a specific point
# n = 4
# obj = Linked_list()
# for i in arr:
#     obj.adding_at_end(i)
# obj.traversal()
# obj.rotate_a_linked_list(n)
# print()
# obj.traversal()


# singly linked list to circular linked list
# arr = list(map(int, input("enter array elements : ").split(' ')))
# obj = Linked_list()
# for i in arr:
#     obj.adding_at_end(i)
# obj.traversal()
# obj.singly_to_circular()
# print()
# target = int(input("Enter how many times you want to print the circular linked list :"))
# obj.travarsal_circular(target)

# arr = arr = list(map(int, input("enter array elements : ").split(' ')))      ## Reverse a Linked List in groups of given size
# target = 4
# obj = Linked_list()
# for i in arr:
#     obj.adding_at_end(i)
# obj.traversal()
# a, b = obj.cut_linked_list_into_specific_portion(target)
# a_rev = a.reversal()
# b_rev = b.reversal()
# a.marge_two_linked_list(b)
# a.traversal()


# singly linked list to looped linked list
arr = list(map(int, input("enter array elements : ").split(' ')))
obj = Linked_list()
for i in arr:
    obj.adding_at_end(i)
obj.traversal()                # 1 2 3 4 5 6 3 4 .......
target = int(input("Enter the node you want to start the loop"))
obj.make_loop(target)
print()
target = int(
    input("Enter how many times you want to print the circular linked list :"))
obj.travarsal_circular(target)
