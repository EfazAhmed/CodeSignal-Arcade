def solution(arr):
    if len(arr) % 2 == 0:
        left = (len(arr) // 2) - 1
        right = len(arr) // 2
        middle = arr[left] + arr[right]
    else:
        mid = len(arr) // 2
        middle = arr[mid]
        
    if arr[0] == arr[-1] == middle:
        return True
    return False
