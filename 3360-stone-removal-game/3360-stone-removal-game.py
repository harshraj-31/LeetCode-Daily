class Solution:
    def canAliceWin(self, n: int) -> bool:
        alice_turn = True
        k = 10
        while k > 0 and n >= k:
            n -= k
            k -= 1
            alice_turn = not alice_turn
        # the player to move can't remove k stones, so they lose
        return not alice_turn