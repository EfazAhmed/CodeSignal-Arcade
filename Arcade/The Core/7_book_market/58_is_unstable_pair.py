def solution(filename1, filename2):
    return (filename1 < filename2) != (filename1.lower() < filename2.lower())

