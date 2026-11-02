# Definition for singly-linked list.
"""Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]"""
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
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None: 
        sorted_list = ListNode(0)
        sorted_list_mover = sorted_list
        
        while list1 and list2:
            if list1.val <= list2.val:
                sorted_list_mover.next = list1
                list1 = list1.next
            else:
                sorted_list_mover.next = list2
                list2 = list2.next
            sorted_list_mover = sorted_list_mover.next
        sorted_list_mover.next = list1 or list2
        return sorted_list.next
    

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
sorted = Solution().mergeTwoLists(list1, list2)
show(sorted)
