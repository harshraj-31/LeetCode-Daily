class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        n = len(nums)
        min_positive_sum = float('inf')

        for i in range(n):
            current_sum = 0
            # Extend right endpoint up to i + r - 1 (max length r)
            max_j = min(n - 1, i + r - 1)
            for j in range(i, max_j + 1):
                current_sum += nums[j]
                length = j - i + 1

                if length >= l and current_sum > 0:
                    if current_sum < min_positive_sum:
                        min_positive_sum = current_sum

        return -1 if min_positive_sum == float('inf') else min_positive_sum