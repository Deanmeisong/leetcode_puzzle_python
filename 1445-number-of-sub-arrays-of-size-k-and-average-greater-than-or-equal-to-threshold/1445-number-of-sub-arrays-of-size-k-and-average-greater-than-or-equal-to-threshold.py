class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        threshold *= k
        s = sum(arr[:k])
        ans = int(s >= threshold)
        for i in range(k, len(arr)):
            s += arr[i] - arr[i - k]
            ans += int(s >= threshold)
        return ans