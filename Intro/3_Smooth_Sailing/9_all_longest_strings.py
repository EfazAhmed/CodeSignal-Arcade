def solution(inputArray):
    max_length = len(max(inputArray, key=len))
    return [element for element in inputArray if len(element) == max_length]
