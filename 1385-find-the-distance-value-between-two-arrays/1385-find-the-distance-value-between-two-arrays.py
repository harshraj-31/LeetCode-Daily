from bisect import bisect_left

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        n = len(arr2)
        count = 0

        for a in arr1:
            i = bisect_left(arr2, a - d)
            if i == n or arr2[i] > a + d:
                count += 1

        return count