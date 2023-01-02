# Beats 98% solutions

import math
class Solution:

    def __init__(self):
        self.final_res = []
        self.iteration_depth = -1

    def getPermutation(self, n: int, k: int, list_opt=[]) -> str:
        registry = []
        if len(list_opt) > 0:
            list_nums = list_opt
            list_nums.sort()
        else:
            list_nums = list(range(1, n + 1))
        if len(list_nums) == 1:
            if self.iteration_depth == -1:
                return str(list_nums[0])
            self.final_res.extend(list_nums)
            return
        digit = n - 1
        while math.factorial(digit) > k:
            registry.append(list_nums[n - digit - 1])
            digit -= 1
        list_nums = sorted(list(set(list_nums) ^ set(registry)))
        factor = math.ceil(k / math.factorial(digit))
        registry.append(list_nums[factor - 1])
        del list_nums[factor - 1]
        if (k % math.factorial(digit)) == 0:
            max_permutation = math.factorial(digit)
            self.iteration_depth += 1
            self.final_res.extend(registry)
            self.getPermutation(len(list_nums), max_permutation, list_opt=list_nums)
        else:
            smaller_by = k - (math.factorial(digit) * (factor - 1))
            self.iteration_depth += 1
            self.final_res.extend(registry)
            self.getPermutation(len(list_nums), smaller_by, list_opt=list_nums)
        str_res = [str(digit) for digit in self.final_res]
        return ''.join(str_res)
