def solution(young, beautiful, loved):
    first = young and beautiful and not loved
    second = loved and (not young or not beautiful)
    return first or second

