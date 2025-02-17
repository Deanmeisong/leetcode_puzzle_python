class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        ans = m = 0
        for _, v in cnt.most_common():
            ans += 1
            m += v
            if m*2 >= len(arr): break
        return ans