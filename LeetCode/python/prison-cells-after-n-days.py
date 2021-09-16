# input:   [0, 1, 0, 1, 1, 0, 0, 1]
# 0:       [0, 1, 0, 1, 1, 0, 0, 1] -> cells
# 1:       [0, 1, 1, 0, 0, 0, 0, 0] -> nextcells
# 2:       [0, 0, 0, 0, 1, 1, 1, 0]

''' Time Limit Exceeded

def prisonAfterNDays(cells, n):
    for k in range(n):
        nextcells = [0] * len(cells)        
        for i in range(1, len(cells)-1):
            if cells[i-1] == cells[i+1]:
                nextcells[i] = 1
            else:
                nextcells[i] = 0        
        cells = nextcells        
    return cells
'''


def prisonAfterNDays(cells, n):
    seen = []
    while n > 0:
        nextcells = [0] * len(cells)        
        for i in range(1, len(cells)-1):
            if cells[i-1] == cells[i+1]:
                nextcells[i] = 1
            else:
                nextcells[i] = 0        
        cells = nextcells
        
        n -= 1
        if cells in seen:
            n %= len(seen)
        else:
            seen.append(cells)

    return cells

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        return prisonAfterNDays(cells, n)