# Top-down dp using memoization

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @cache
        def calculate(idx, count_a, turn_a, M):
            res = float('-inf') if turn_a else float('inf')
            if idx >= len(piles):
                return 0
            if turn_a:
                for i in range(idx, idx + 2 * M):
                    k = sum(piles[idx: i + 1]) + calculate(i + 1, count_a, not turn_a, max((i + 1 - idx), M))
                    if k > res:
                        res = k
                        n_idx = i + 1
            else:
                for i in range(idx, idx + 2 * M):
                    m = calculate(i + 1, count_a, not turn_a, max((i + 1 - idx), M))
                    if m < res:
                        res = m
                        n_idx = i + 1
            return res
        return calculate(0, 0, True, 1)
