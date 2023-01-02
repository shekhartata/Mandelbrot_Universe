# Beats 99% solutions -- Dynamic programming approach

class Solution:
    def __init__(self):
        self.length = 0

    def numTrees(self, n: int) -> int:
        lookup = {0: 1, 1: 1}
        for i in range(2, n + 1):
            lsr = 0
            grt = 0
            for j in range(1, i + 1):
                if j != 1:
                    lsr = len(list(range(1, j)))
                grt = len(list(range(j + 1, i + 1)))
                self.length += lookup[lsr] * lookup[grt]
            lookup[i] = self.length
            self.length = 0
        return lookup[n]
