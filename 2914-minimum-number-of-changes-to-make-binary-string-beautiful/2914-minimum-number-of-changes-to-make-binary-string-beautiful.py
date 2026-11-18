class Solution:
    def minChanges(self, s: str) -> int:
        x = int(s, 2)
        mask = ((1 << len(s)) - 1) // 3
        return ((x ^ (x >> 1)) & mask).bit_count()