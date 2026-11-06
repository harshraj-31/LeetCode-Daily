from typing import List

class Solution:
    def countZeroRequestServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda v: v[1])
        order = sorted(range(len(queries)), key=lambda i: queries[i])
        cnt = [0] * (n + 1)
        active = 0
        res = [0] * len(queries)
        left = right = 0
        m = len(logs)
        for idx in order:
            q = queries[idx]
            while right < m and logs[right][1] <= q:
                srv = logs[right][0]
                if cnt[srv] == 0:
                    active += 1
                cnt[srv] += 1
                right += 1
            while left < m and logs[left][1] < q - x:
                srv = logs[left][0]
                cnt[srv] -= 1
                if cnt[srv] == 0:
                    active -= 1
                left += 1
            res[idx] = n - active
        return res

    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        return self.countZeroRequestServers(n, logs, x, queries)