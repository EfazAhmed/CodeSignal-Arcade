def solution(a):
    ids = [i for i in range(len(a)) if a[i] == -1]
    sorted_ppl = sorted([person for person in a if person != -1])
    
    answer = []
    for i in range(len(a)):
        if i in ids:
            answer.append(-1)
        else:
            answer.append(sorted_ppl[0])
            sorted_ppl.pop(0)
    
    return answer