class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        best = inc = dec = 1
        prev = nums[0]

        for x in nums[1:]:
            if x > prev:
                inc += 1
                dec = 1
            elif x < prev:
                dec += 1
                inc = 1
            else:
                inc = dec = 1

            if inc > best:
                best = inc
            if dec > best:
                best = dec

            prev = x

        return best