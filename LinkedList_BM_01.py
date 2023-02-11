# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, head):
        curr = head
        zero = 0
        one = 0
        while curr:
            if curr.val==1:
                one+=1
            else:
                zero+=1
            curr = curr.next
        curr = head
        for i in range(zero):
            curr.val = 0
            curr = curr.next
        for i in range(one):
            curr.val = 1
            curr = curr.next
        return head
ll1
