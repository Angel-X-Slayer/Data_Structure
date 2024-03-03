class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class linked_list:
    def __init__(self):
        self.head = None

    def adding_at_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.ref != None:
                n = n.ref
            n.ref = new_node

    def traversal(self):
        if self.head == None:
            print("empty linked List")
        else:
            n = self.head
            while n != None:
                print(n.data, end=" -> ")
                n = n.ref


def reverse_by_given_size(self, target):

    pass


# Reverse a Linked List in groups of given size
arr = arr = list(map(int, input("enter array elements : ").split(' ')))
target = 4
obj = linked_list()
for i in arr:
    obj.adding_at_end(i)
obj.traversal()
obj.reverse_by_given_size(target)


# a, b = obj.cut_linked_list_into_specific_portion(target)
# a_rev = a.reversal()
# b_rev = b.reversal()
# a.marge_two_linked_list(b)
# a.traversal()
