# Top-down Dp, beats 70p

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        self.res = list()
        memo = dict()
        def calculate(piles, idx, alice_turn = True, count_a = 0, count_b = 0, dir = None):
            if memo.get((str(piles), dir)):
                return memo[(str(piles), dir)]
            if alice_turn:
                count_a += piles[idx]
            else:
                count_b += piles[idx]
            if len(piles) > 1:
                if idx == 0:
                    memo[(str(piles), "l")] = calculate(piles[1:], 0, not alice_turn, count_a, count_b, "l")
                    memo[(str(piles), "r")] = calculate(piles[1:], -1, not alice_turn, count_a, count_b, "r")
                if idx < 0:
                    memo[(str(piles), "r")] = calculate(piles[:len(piles) - 1], -1, not alice_turn, count_a, count_b, "r")
                    memo[(str(piles), "l")] = calculate(piles[:len(piles) - 1], 0, not alice_turn, count_a, count_b, "l")
            else:
                if (count_a, count_b) not in self.res:
                    self.res.append((count_a, count_b))
                return (count_a, count_b)
        calculate(piles, 0, True, 0, 0)
        calculate(piles, -1, True, 0, 0)
        for item in self.res:
            if item[0] > item[1]:
                return True
        return False
