def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    if min(yourLeft, yourRight) == min(friendsLeft, friendsRight):
        if max(yourLeft, yourRight) == max(friendsLeft, friendsRight):
            return True
    return False
