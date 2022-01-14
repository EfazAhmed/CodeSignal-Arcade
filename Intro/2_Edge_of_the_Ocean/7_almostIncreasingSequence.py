def solution(sequence):
    i = 0
    while i < len(sequence) - 1:
        if not sequence[i] < sequence[i + 1]:
            if increasingSequence(sequence[:i] + sequence[i+1:]) or increasingSequence(sequence[:i+1] + sequence[i+2:]):
                return True
            else:
                return False
        i += 1
    return True
        
def increasingSequence(s):
    for i in range(len(s)-1):
        if s[i] >= s[i+1]:
            return False
    return True