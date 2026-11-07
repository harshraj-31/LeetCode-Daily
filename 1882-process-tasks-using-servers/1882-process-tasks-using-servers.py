from heapq import heapify, heappush, heappop

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        free = [(w, i) for i, w in enumerate(servers)]
        heapify(free)
        busy = []
        ans = [0] * len(tasks)
        time = 0

        for j, duration in enumerate(tasks):
            if time < j:
                time = j
            if not free:
                time = busy[0][0]

            while busy and busy[0][0] <= time:
                _, w, i = heappop(busy)
                heappush(free, (w, i))

            w, i = heappop(free)
            heappush(busy, (time + duration, w, i))
            ans[j] = i

        return ans