class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        ans = -inf
        dirs= (1,-1,-1,1,1)
        for a, b in pairwise(dirs):
            mx, mi = -inf, inf
            for i, (x,y) in enumerate(zip(arr1, arr2)):
                mx = max(mx, a*x+b*y+i)
                mi = min(mi, a*x+b*y+i)
                ans = max(mx-mi,ans)
        return ans