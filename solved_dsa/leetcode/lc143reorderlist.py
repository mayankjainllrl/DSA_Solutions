
def show(head):
    listy = []
    node = head
    while node:
        listy.append(str(node.val))
        node = node.next    
    print((" -> ".join(listy) + " -> None"))
        
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
"""My Solution Not Optimal Space Complexity O(n)"""
# class Solution:
#     def reorderList(self, head: ListNode | None) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         listy = []
#         node = head
#         len_list = 0
#         while node:
#             listy.append(node)
#             node = node.next
#             len_list += 1
            
#         node = head
#         half_len = len_list // 2
#         while half_len:
#             node = node.next
#             half_len -= 1
#         node.next = None
        
#         list_bound = (len_list // 2) * -1
#         if len_list % 2 == 0:
#             list_bound += 1
#         l_i = -1
#         node = head
#         while l_i >= list_bound: 
#             node_next = node.next
#             node.next = listy[l_i]
#             node.next.next = node_next
#             l_i -= 1
#             node = node.next.next


# Optimal Solution with hint
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        slow.next = None
        rev_list = None
        while second_half:
            node_nxt = second_half.next
            second_half.next = rev_list
            rev_list = second_half
            second_half = node_nxt
        
        node = head
        while rev_list:
            rev_list_next, node_nxt = rev_list.next, node.next
            node.next = rev_list
            node.next.next = node_nxt
            rev_list = rev_list_next
            node = node_nxt

    
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
show(head)
Solution().reorderList(head)
show(head)  
