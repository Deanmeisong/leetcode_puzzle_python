class Solution(object):
    def removeOnes(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        s = set()
        for row in grid:
            t = tuple(row) if grid[0][0] == row[0] else tuple(x^1 for x in row)
            s.add(t)
        return len(s) == 1