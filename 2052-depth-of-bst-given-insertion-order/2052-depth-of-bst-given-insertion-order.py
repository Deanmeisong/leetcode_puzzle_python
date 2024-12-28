from sortedcontainers import SortedDict

class Solution(object):
    def maxDepthBST(self, order):
        inf = float('inf')
        # Initialize the SortedDict
        sd = SortedDict({0: 0, inf: 0, order[0]: 1})
        ans = 1

        # Traverse the insertion order
        for v in order[1:]:
            lower = sd.bisect_left(v) - 1  # Index of item just smaller than v
            higher = lower + 1            # Index of item just larger (or equal) than v
            # In sortedcontainers, sd.values() returns a ValuesList that supports indexing
            depth = 1 + max(sd.values()[lower], sd.values()[higher])
            ans = max(ans, depth)
            # Insert new value
            sd[v] = depth

        return ans
