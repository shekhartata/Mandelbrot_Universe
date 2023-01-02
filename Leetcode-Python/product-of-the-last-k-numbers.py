# Beats 95% solutions

class ProductOfNumbers:

    def __init__(self):
        self.k = []
        self.cacher = [1]
        self.ctr = 0
        self.len = 0

    def add(self, num: int) -> None:
        self.k.append(num)
        if num != 0:
            self.cacher.append(self.cacher[-1] * num)
            self.len += 1
        else:
            self.cacher.append(1)
            self.len = 0
            self.ctr = len(self.cacher) - 1

    def getProduct(self, k: int) -> int:
        prod = 1
        if k > self.len:
            return 0
        divider = self.ctr + (self.len - k)
        return int(self.cacher[-1] / self.cacher[divider])

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)