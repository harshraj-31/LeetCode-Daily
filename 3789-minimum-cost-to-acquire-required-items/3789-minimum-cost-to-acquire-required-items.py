class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        paired = min(need1, need2)
        total = paired * min(costBoth, cost1 + cost2)

        if need1 > need2:
            total += (need1 - need2) * min(cost1, costBoth)
        else:
            total += (need2 - need1) * min(cost2, costBoth)

        return total