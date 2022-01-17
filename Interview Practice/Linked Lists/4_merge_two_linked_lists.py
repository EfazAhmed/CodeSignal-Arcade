# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l1, l2):
    
    head = ListNode(-1)
    curr = head
    
    while True:
        if l1 and l2:
            if l1.value > l2.value:
                curr.next = l2
                curr = curr.next
                l2 = l2.next
            else:
                curr.next = l1
                curr = curr.next
                l1 = l1.next
        elif l1:
            curr.next = l1
            curr = curr.next
            l1 = l1.next
        elif l2:
            curr.next = l2
            curr = curr.next
            l2 = l2.next
        else:
            break
    
    return head.next
            
