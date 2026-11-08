class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row_count = [sum(row) for row in grid]
        col_count = [sum(col) for col in zip(*grid)]

        total = 0
        for i, row in enumerate(grid):
            if row_count[i] > 1:
                total += row_count[i]
            else:
                for j, v in enumerate(row):
                    if v and col_count[j] > 1:
                        total += 1
                        break

        return total