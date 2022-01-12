def solution(time):
    hours = int(time[0:2])
    minutes = int(time[3:])
    
    if hours >= 0 and hours <= 23:
        if minutes >= 0 and minutes <= 59:
            return True
            
    return False
    
