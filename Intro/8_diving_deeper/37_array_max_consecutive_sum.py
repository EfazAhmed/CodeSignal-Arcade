def solution(inputArray, k):
    rolling_sum = sum(inputArray[0:k])
    max_ = rolling_sum
    for i in range(len(inputArray)-k):
        rolling_sum += inputArray[i+k] - inputArray[i]
        max_ = max(max_, rolling_sum)
    return max_
