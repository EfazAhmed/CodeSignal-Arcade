def solution(name):
    if name[0].isdigit():
        return False
    else:
        for char in name:         
            if not char.isalnum() and char != "_":
                return False
        return True
