def solution(arr):
    if len(arr) <= 1:
        return arr
    temp = arr[-1]
    arr[-1] = arr[0]
    arr[0] = temp
    return arr