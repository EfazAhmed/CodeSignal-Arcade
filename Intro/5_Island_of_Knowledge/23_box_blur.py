def solution(image):
    length = len(image[0])
    height = len(image)
    
    
    averages = []
    
    
    for j in range(height-2):
        sub = []
        for i in range(length-2):
            sum = 0
            sum += image[j][i]
            sum += image[j][i+1]
            sum += image[j][i+2]
            sum += image[j+1][i]
            sum += image[j+1][i+1]
            sum += image[j+1][i+2]
            sum += image[j+2][i]
            sum += image[j+2][i+1]
            sum += image[j+2][i+2]
            sub.append(int(sum/9))
        averages.append(sub)
        
    return averages
        