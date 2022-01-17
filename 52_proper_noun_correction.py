def solution(noun):
    if len(noun) == 1:
        return noun.upper()
    return noun[0].upper() + noun[1:].lower()
