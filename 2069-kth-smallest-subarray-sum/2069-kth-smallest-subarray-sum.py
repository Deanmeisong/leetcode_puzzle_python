class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        def f(s):
            j = t = cnt = 0
            for i in range(len(nums)):
                t += nums[i]
                while t > s:
                    t -= nums[j]
                    j += 1
                cnt += i-j+1
            return cnt >= k
        
        l, r = min(nums), sum(nums)
        return l + bisect_left(range(l, r + 1), True, key=f)
