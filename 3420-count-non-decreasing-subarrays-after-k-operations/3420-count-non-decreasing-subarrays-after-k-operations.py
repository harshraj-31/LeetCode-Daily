from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i, v in enumerate(nums):
            prefix[i + 1] = prefix[i] + v

        segments = deque()
        total = 0
        r = n - 1
        ans = 0

        for l in range(n - 1, -1, -1):
            x = nums[l]

            while segments and segments[0][1] <= x:
                s, v = segments.popleft()
                e = segments[0][0] - 1 if segments else r
                total -= v * (e - s + 1)

            end = segments[0][0] - 1 if segments else r
            total += x * (end - l + 1)
            segments.appendleft((l, x))

            while total - (prefix[r + 1] - prefix[l]) > k:
                s, v = segments[-1]
                total -= v
                if s == r:
                    segments.pop()
                r -= 1

            ans += r - l + 1

        return ans