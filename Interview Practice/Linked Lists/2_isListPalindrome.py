# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(head):
    
    slow, fast = head,head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    rev = reverse(slow)

    while head is not None and rev is not None:
        if head.value != rev.value:
            break
        
        head = head.next
        rev = rev.next

    if head is None or rev is None:
        return True

    return False


def reverse(head):
    prev = None
    while head:
        next_value = head.next
        head.next = prev
        prev = head
        head = next_value
    return prev