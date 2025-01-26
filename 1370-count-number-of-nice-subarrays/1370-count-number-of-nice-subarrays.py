class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cnt = Counter({0:1})
        ans = t = 0
        for x in nums:
            t += x&1
            if t >= k:
                ans += cnt[t-k]
            cnt[t] += 1
        return ans