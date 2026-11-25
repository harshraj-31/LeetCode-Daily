import random
from collections import Counter

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        M = (1 << 61) - 1
        B = random.randrange(10**6, M - 1)

        pre = [0] * (n + 1)
        pw = [1] * (n + 1)
        for i, x in enumerate(nums):
            pre[i + 1] = (pre[i] * B + x) % M
            pw[i + 1] = pw[i] * B % M

        def has_unique(L: int) -> bool:
            cnt = Counter((pre[i + L] - pre[i] * pw[L]) % M
                          for i in range(n - L + 1))
            return any(v == 1 for v in cnt.values())

        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if has_unique(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo