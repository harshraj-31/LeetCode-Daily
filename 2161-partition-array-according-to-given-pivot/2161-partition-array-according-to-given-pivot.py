class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = [v for v in nums if v < pivot]
        greater = [v for v in nums if v > pivot]
        return less + [pivot] * (len(nums) - len(less) - len(greater)) + greater