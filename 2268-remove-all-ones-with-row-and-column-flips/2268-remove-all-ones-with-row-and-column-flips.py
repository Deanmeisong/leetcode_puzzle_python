class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        s = set()
        for row in grid:
            t = tuple(row) if grid[0][0] == row[0] else tuple(x^1 for x in row)
            s.add(t)
        return len(s) == 1