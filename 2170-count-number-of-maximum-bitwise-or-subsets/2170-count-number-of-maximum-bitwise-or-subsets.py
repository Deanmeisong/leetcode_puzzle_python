class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans = mx = 0
        for x in nums:
            mx |= x
        def dfs(i, t):
            nonlocal ans, mx
            if i == len(nums):
                if mx == t:
                    ans += 1
                return
            dfs(i+1, t|nums[i])
            dfs(i+1, t)
        dfs(0,0)
        return ans