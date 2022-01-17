def solution(address):
    address = address[::-1]
    idx = address.find("@")
    part = address[:idx][::-1]
    return part
