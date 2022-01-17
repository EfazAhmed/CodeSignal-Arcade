import numpy as np

def solution(n):
    square_root = pow(n, 1/2)
    cube_root = np.cbrt(n)
    if square_root == int(square_root) or cube_root == int(cube_root):
        return True
        
    return False
