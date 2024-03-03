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


def merge_two_ll(ll1, ll2):
    resultnode = Node(0)
    tail = resultnode
    while True:
        if ll1 == None:
            tail.ref = ll2
            break
        if ll2 == None:
            tail.ref = ll1
            break
        if ll1.data <= ll2.data:
            tail.ref = ll1
            ll1 = ll1.ref
        else:
            tail.ref = ll2
            ll2 = ll2.ref
        tail = tail.ref
    return (resultnode.ref)


def traversal1(ll1):
    if ll1.head == None:
        print("empty linked List")
    else:
        n = ll1.head.data
        while n != None:
            print(n.data, end=" -> ")
            n = n.ref


arr = arr = list(map(int, input("enter array elements : ").split(' ')))
ll1 = linked_list()
for i in arr:
    ll1.adding_at_end(i)
ll1.traversal()
print()
arr = arr = list(map(int, input("enter array elements : ").split(' ')))
ll2 = linked_list()
for i in arr:
    ll2.adding_at_end(i)
ll2.traversal()
print()
# here if we use ll1 instade of ll1.head, that means the merge_two_ll will
ll1.head = merge_two_ll(ll1.head, ll2.head)
# return a linked list which will be stored in a completely new linked list object
print(ll1.traversal())
# without any attribute or function,thats why it will throw an error that ll1 has
# attribute traversal().


'''why i should use ll1.head on the 70th line instade of ll1?


In the given code, the merge_two_ll function returns a linked list (specifically, the head node of the merged list). When merging two linked lists, it is necessary to update the head attribute of the linked_list object to the new merged list.

On line 70, the code uses ll1.head = merge_two_ll(ll1.head, ll2.head) to update the head attribute of the linked_list object ll1 to the head node of the merged list.

If we were to use ll1 instead of ll1.head in this line, we would be assigning the entire merged linked list to the ll1 object, rather than just updating its head attribute. This would cause issues when trying to call the traversal method on ll1, as this method expects the head attribute to be a node object, not a linked list object.

Therefore, using ll1.head instead of ll1 in line 70 is necessary to ensure that the traversal method can be called correctly on the ll1 object.'''
