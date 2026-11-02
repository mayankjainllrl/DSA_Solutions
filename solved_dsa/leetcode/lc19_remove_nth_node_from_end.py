# Definition for singly-linked list.

def show(node):
    parts = []
    while node:
        parts.append(str(node.val))
        node = node.next 
    
    print(" -> ".join(parts) + " -> None")


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        i = 0
        n_list = ListNode(0)
        n_list.next = head
        node = head
        n_list_mover = n_list
        while node:
            if i >= n:
                n_list_mover = n_list_mover.next
            else:
                i += 1
            node = node.next
        n_list_mover.next = n_list_mover.next.next
        return n_list.next
    
n = 2
# head = ListNode(1, ListNode(2, ListNode(4, ListNode(5, ListNode(6, ListNode(8, ListNode(9, ListNode(4, ListNode(2, ListNode(1))))))))))
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
show(head)
sol = Solution().removeNthFromEnd(head, n)
show(sol)