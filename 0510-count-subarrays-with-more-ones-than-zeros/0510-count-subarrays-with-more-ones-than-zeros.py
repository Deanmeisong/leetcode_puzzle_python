class BinaryIndexTree:
    __slots__ = ["n", "c"]
    def __init__(self, n: int):
        self.n = n
        self.c = [0] * (n+1)
    
    def update(self, x: int, v:int):
        while x <= self.n:
            self.c[x] += v
            x += x & -x

    def query(self, x:int):
        ans = 0
        while x:
            ans += self.c[x]
            x -= x & -x
        return ans

class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        n = len(nums)
        base = n+1
        tree = BinaryIndexTree(base+n)
        tree.update(base,1)
        mod = 10**9 + 7
        ans = s = 0
        for x in nums:
            s += x or -1
            ans += tree.query(s-1+base)
            ans %= mod
            tree.update(s+base,1)
        return ans
