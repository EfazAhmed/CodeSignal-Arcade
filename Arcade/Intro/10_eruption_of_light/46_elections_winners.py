def solution(votes, k):
    winners = 0
    
    votes.sort()
    
    for i in range(len(votes)):
        
        if i < len(votes) - 1:
            value = votes[i] + k
            if value > votes[-1]:
                winners += 1
                continue
        else:
            old = votes[i]
            new = votes[i] + k
            votes[i] = new
            max_ = max(votes)
            
            if votes.count(max_) == 1 and max_ == new:
                winners += 1
    
            votes[i] = old
    
    
  
    
    return winners
