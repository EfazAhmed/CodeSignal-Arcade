# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(a, b):
    nums_a = []
    nums_b = []
        
    while a:
        nums_a.append(str(a.value))
        if a.next:
            a = a.next
        else:
            break
    
    while b:
        nums_b.append(str(b.value))
        if b.next:
            b = b.next
        else:
            break
    
    int_a = createBigInteger(nums_a)
    int_b = createBigInteger(nums_b)
    total = str(int_a + int_b)
    print(int_a)
    print(int_b)
    print(total)
    return createList(total)


def createBigInteger(li):
    temp = ""
    for el in li:
        word = el
        while len(word) < 4:
            word = "0" + word
        temp += word
    return int(temp)    


def createList(num):
    if len(num) <= 4:
        return [int(num)]
    else:
        temp = num[-4:]
        idx = -1
        for i, letter in enumerate(temp):
            if letter != '0':
                idx = i
                break
        if idx == -1:
            temp =  int(temp)
        else:
            temp = int(temp[idx:])
        return createList(num[:-4]) + [temp]
        
        
