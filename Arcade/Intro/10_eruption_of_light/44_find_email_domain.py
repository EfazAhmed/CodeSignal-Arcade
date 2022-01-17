def solution(address):
    rev = address[::-1]
    idx = rev.index("@")
    domain = rev[:idx][::-1]
    return domain
