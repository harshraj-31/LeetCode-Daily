class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        INF = 1 << 60
        a, b, c = INF, INF, 0

        for j in range(n):
            a, b, c = b, c, costs[j] + min(c + 1, b + 4, a + 9)

        return c