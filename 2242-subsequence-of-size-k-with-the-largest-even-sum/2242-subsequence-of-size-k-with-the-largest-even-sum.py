class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = sum(nums[-k:])
        if ans%2 == 0: return ans
        n = len(nums)
        mx1 = mx2 = -inf
        for x in nums[:n-k]:
            if x&1:
                mx1 = x
            else: mx2 = x
        mi1 = mi2 = inf
        for x in nums[-k:][::-1]:
            if x&1:
                mi1 = x
            else: mi2 = x
        ans = max(ans-mi1+mx2, ans-mi2+mx1,-1)
        
        return -1 if ans < 0 else ans
        
        