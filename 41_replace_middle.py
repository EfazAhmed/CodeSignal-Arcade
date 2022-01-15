def solution(arr):
    if len(arr) % 2 == 1:
        return arr
    else:
        left = (len(arr) // 2) - 1
        right = len(arr) // 2
        total = arr[left] + arr.pop(right)
        arr[left] = total
        return arr