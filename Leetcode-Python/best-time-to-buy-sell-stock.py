# Using heaps, beats 68p

import heapq
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.profit = 0
        self.k = list()
        for itr, item in enumerate(prices):
            self.k.append((-1 * item, itr ))
        heapq.heapify(self.k)
        def calculate(arr, idx):
            minima = 1000000
            for i in range(len(arr)):
                if arr[i] < minima:
                    minima = arr[i]
                    while len(self.k):
                        m = heapq.heappop(self.k)
                        if m[1] > i:
                            self.profit = max(self.profit, (-1 * m[0]) - arr[i])
                            heapq.heappush(self.k, m)
                            break
        calculate(prices, 0)
        return self.profit
