def solution(n):
    curr = 0
    temp = str(n)
    while True:
        if len(temp) == 1:
            return curr
        else:
            sum_ = 0
            for letter in temp:
                sum_ += int(letter)
            temp = str(sum_)
            curr += 1