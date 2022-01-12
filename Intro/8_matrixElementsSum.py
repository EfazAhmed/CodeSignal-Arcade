def solution(matrix):
    sum = 0
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            if matrix[row][col] == 0:
                break
            else:
                sum += matrix[row][col]
    return sum