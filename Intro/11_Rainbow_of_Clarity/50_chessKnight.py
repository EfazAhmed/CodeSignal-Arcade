def solution(cell):
    letter = ord(cell[0])
    number = int(cell[1])
    
    all_moves = []
    
    all_moves.append(f"{chr(letter-2)}{number+1}")
    all_moves.append(f"{chr(letter-2)}{number-1}")
    
    all_moves.append(f"{chr(letter-1)}{number+2}")
    all_moves.append(f"{chr(letter-1)}{number-2}")
    
    all_moves.append(f"{chr(letter+1)}{number+2}")
    all_moves.append(f"{chr(letter+1)}{number-2}")
    
    all_moves.append(f"{chr(letter+2)}{number+1}")
    all_moves.append(f"{chr(letter+2)}{number-1}")

    count = 0

    print(all_moves)
    for i in range(len(all_moves)):
        print(all_moves[i])
        if all_moves[i][0].isalpha():
            print("alpha")
            if ord(all_moves[i][0]) > 96 and ord(all_moves[i][0]) < 105:
                print("alpha-zone")
                if all_moves[i][1:].isdigit():
                    print("digit")
                    if int(all_moves[i][1:]) < 9 and int(all_moves[i][1:]) > 0:
                        print("digit-zone")
                        count += 1
    return count