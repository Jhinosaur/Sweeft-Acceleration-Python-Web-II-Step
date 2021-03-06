import math
import random
import re

def bomberMan(n, grid):    # n = how many seconds pass
    if n == 1:
        return grid

    if n%2 == 0:
        return ['O'*c for i in range(r)]

    n //= 2
    for q in range((n+1) % 2 + 1):
        newgrid = [['O']*c for i in range(r)]

        def set(x,y):       # detonation
            if 0<=x<r and 0<=y<c:
                newgrid[x][y] = '.'

        xi = [0,0,0,1,-1]
        yi = [0,-1,1,0,0]

        for x in range(r):
            for y in range(c):
                if grid[x][y] == 'O':
                    for i,j in zip(xi, yi):
                        set(x+i,y+j)

        grid = newgrid

    return ["".join(x) for x in grid]

