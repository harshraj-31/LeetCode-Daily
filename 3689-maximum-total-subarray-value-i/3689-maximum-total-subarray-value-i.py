from typing import List

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return k * (max(nums) - min(nums))

    # optional alias if needed
    def maximumTotalSubarrayValue(self, nums: List[int], k: int) -> int:
        return self.maxTotalValue(nums, k)