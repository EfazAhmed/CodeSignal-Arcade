def solution(n, m):
    return (n + m + getGCD(n,m)) - 2
    
def getGCD(x, y):
   while(y):
       x, y = y, x % y
   return x