class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        last = [-1] * 26          # nearest ancestor on current path per char
        new_parent = parent[:]
        saved = [-1] * n          # previous last[c] to restore on exit
        order = []

        stack = [(0, False)]
        while stack:
            u, leaving = stack.pop()
            c = ord(s[u]) - 97
            if leaving:
                last[c] = saved[u]
                continue
            order.append(u)
            if last[c] != -1:
                new_parent[u] = last[c]
            saved[u] = last[c]
            last[c] = u
            stack.append((u, True))
            for v in children[u]:
                stack.append((v, False))

        size = [1] * n
        for u in reversed(order):
            if u != 0:
                size[new_parent[u]] += size[u]
        return size