def solution(commands):
    students = [3, 3]
    count = 0
    for command in commands:
        students[0] = getNextPos(students[0], command, False)
        students[1] = getNextPos(students[1], command, True)
        if students[0] == students[1]:
            count += 1
    return count
        
def getNextPos(current, turn, isConfused):
    if isConfused == False:
        if turn == "L":
            if current == 1:
                return 4
            elif current == 2:
                return 1
            elif current == 3:
                return 2
            else:
                return 3
        elif turn == "R":
            if current == 1:
                return 2
            elif current == 2:
                return 3
            elif current == 3:
                return 4
            else:
                return 1
        elif turn == "A":
            if current == 1:
                return 3
            elif current == 2:
                return 4
            elif current == 3:
                return 1
            else:
                return 2
    else:
        if turn == "L":
            if current == 1:
                return 2
            elif current == 2:
                return 3
            elif current == 3:
                return 4
            else:
                return 1
        elif turn == "R":
            if current == 1:
                return 4
            elif current == 2:
                return 1
            elif current == 3:
                return 2
            else:
                return 3
        elif turn == "A":
            if current == 1:
                    return 3
            elif current == 2:
                return 4
            elif current == 3:
                return 1
            else:
                return 2