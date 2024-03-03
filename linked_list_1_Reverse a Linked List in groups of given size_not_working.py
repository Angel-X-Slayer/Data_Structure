'''
the approach was simple, just cut the linked list by the target using cut_linked_list function.
reverse all the linked list using reversal function,and store the head in different variable.
then call the marge funtion and merge the linked list.
But this approach is not full proof, we cant achive the desired output.
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


def marge_two_linked_list(ll1, ll2):
    n = ll1
    while n != None:
        n = n.ref
    n.ref = ll2
    return (ll1)


def reversal(ll1):
    prev = None
    n = ll1.ref
    while n != None:
        next = n.ref
        n.ref = prev
        prev = n
        n = next
    ll1.ref = prev
    return (ll1)


def traversal(ll1):
    if ll1.ref == None:
        print("empty linked List")
    else:
        n = ll1
        while n != None:
            print(n.data, end=" -> ")
            n = n.ref


class Linked_list:
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

    def cut_linked_list_into_specific_portion(self, target):
        n = self.head
        count = 0
        while n.ref != None and count < target:
            n = n.ref
            count += 1

        k = n.ref
        return (self.head, k)


# arr = arr = list(map(int, input("enter array elements : ").split(' ')))
arr = [1, 2, 3, 4, 5, 6, 7, 8]
target = 4
obj = Linked_list()
for i in arr:
    obj.adding_at_end(i)
obj.traversal()
print()
a, b = obj.cut_linked_list_into_specific_portion(target)
traversal(a)
print()
traversal(b)
a_rev = reversal(a)
b_rev = reversal(b)
traversal(a_rev)
print()
traversal(b_rev)
k = marge_two_linked_list(a_rev, b_rev)
traversal(k)
