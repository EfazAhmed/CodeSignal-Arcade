def solution(candlesNumber, makeNew):
    totalLeftovers = 0
    totalSolutions = 0
    
    while True:
        totalSolutions += candlesNumber
        totalLeftovers += candlesNumber
        candlesNumber = 0
        candlesNumber = totalLeftovers // makeNew
        totalLeftovers = totalLeftovers % makeNew
        if candlesNumber == 0:
            break
            
    return totalSolutions
        
