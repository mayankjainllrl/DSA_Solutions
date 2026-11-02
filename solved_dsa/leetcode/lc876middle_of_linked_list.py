# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        mid = head
        node = head
        while node and node.next:
            mid = mid.next
            node = node.next.next
        return mid
    
    
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

print(Solution().middleNode(head).val)