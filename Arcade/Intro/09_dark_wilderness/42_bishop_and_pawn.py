def solution(bishop, pawn):
    bish_ltr = bishop[0]
    bish_num = int(bishop[1])
    pawn_ltr = pawn[0]
    pawn_num = int(pawn[1])
    
    bish_ltr_n = ord(bish_ltr) - 64
    pawn_ltr_n = ord(pawn_ltr) - 64
    ltr_diff = abs(bish_ltr_n - pawn_ltr_n)
    num_diff = abs(bish_num - pawn_num)

    return ltr_diff / num_diff == 1