def solution(n):
    if str(n).count("0") == len(str(n)) - 1:
        return n
    else:
        s = [x for x in str(n)]
        for i in range(len(s)-1,0,-1):
            if s[i] != "0":
                if int(s[i]) < 5:
                    s[i] = "0"
                else:
                    s[i] = "0"
                    s[i-1] = str(int(s[i-1]) + 1)
        join = "".join(s)
        return solution(int(join))