# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        rev_list = None
        node = head
        while node:
            node_next = node.next
            node.next = rev_list
            rev_list = node
            node = node_next
        return rev_list
    

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print(Solution().reverseList(head))
