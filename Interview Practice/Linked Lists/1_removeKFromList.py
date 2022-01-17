#Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None
    

def solution(l, k):
    
    while l is not None and l.value == k:
        l = l.next
        
    curr = l
    while curr is not None and curr.next is not None:
        if curr.next.value == k:
            curr.next = curr.next.next
        else:
            curr = curr.next
            
    return l
            