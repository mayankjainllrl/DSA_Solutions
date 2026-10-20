# Lab step 1
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

def show(node):
    parts = []
    while node:
        parts.append(str(node.val))
        node = node.next 
    
    print(" -> ".join(parts) + " -> None")
    
show(head)
show(head)

# Lab step 2
finger = head
finger = finger.next
show(head)        # prediction: 1 -> 2 -> 3 -> 4 -> None, I think because the name head is pointing 1 and name finger is pointing 2 I might be wrong but this is what I think

# prediction A result correct

# let me try to print finger also my prediction that it will print: 2 -> 3 -> 4 -> None
show(finger) # correctly predicted the result.

head.next = head.next.next
show(head)        # prediction 1 -> 3 -> 3 -> 4 -> None, Not sure but I think this.

# prediction B incorrect Ok I am started to understand it better now...... 

# After B I am not sure what will happen with 2 hmmm..... but I think that finger can reach it as I believe that it is pointing towards the box not the value inside it so even if the value inside it changes finger will point to the box and will point at new value.

# so after running it now I am think that this is what happened I believe that the box 2 is same but now it was replaced with box 3 and since finger was pointing at box 2 I believe if I print finger now it should print: 3 -> 4 -> None

show(finger)

# wow completely unexpected hmmm so Maybe I got it wrongly it did not worked as my expectations

finger.next = None
show(head)
show(finger)