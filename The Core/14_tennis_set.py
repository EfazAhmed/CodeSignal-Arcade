def solution(score1, score2):
    li = [score1, score2]
    
    if max(score1, score2) == 6:
        if min(score1,score2) < 5:
            return True
    elif max(score1, score2) > 7:
        return False
    elif max(score1, score2) == 7:
        if min(score1, score2) == 7:
            return False
        elif min(score1, score2) < 5:
            return False
        return True

        
    return False