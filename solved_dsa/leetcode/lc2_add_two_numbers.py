from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build(nums):                      # [2,4,3] -> 2→4→3 chain
    dummy = ListNode()
    tail = dummy
    for n in nums:
        tail.next = ListNode(n)
        tail = tail.next
    return dummy.next        

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getNumberEquivalent(arr):
            multiply_10s = 1
            number_equivalent = 0
            node = arr
            while node:
                number_equivalent = number_equivalent + (node.val * multiply_10s)
                multiply_10s *= 10
                node = node.next
            return number_equivalent

        sum_of_nums = getNumberEquivalent(l1) + getNumberEquivalent(l2)

        result_arr = []
        while sum_of_nums/10 > 0:
            result_arr.append(sum_of_nums % 10)
            sum_of_nums = int(sum_of_nums/10)
        
        print(result_arr)

        dummy = ListNode()
        tail = dummy
        for n in result_arr:
            tail.next = ListNode(n)
            tail = tail.next
        return dummy
    

l1 = [2, 4, 3]
l2 = [5, 6, 4]
s = Solution()
result = s.addTwoNumbers(build(l1), build(l2))
print(result)
 