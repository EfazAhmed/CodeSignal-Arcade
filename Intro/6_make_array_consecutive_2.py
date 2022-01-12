def solution(statues):
    mini = min(statues)
    maxi = max(statues)
    diff = maxi - mini
    return diff - len(statues) + 1