# Beats 96% solutions


def trap(self, height: List[int]) -> int:
    max_height = max(height)
    if height.count(max_height) == 1 and height.index(max_height) == 0:
        result = self.find_trap_water(height, len(height) - 1, -1, -1)
    elif height.count(max_height) == 1 and height.index(max_height) == len(height) - 1:
        result = self.find_trap_water(height, 0, len(height), 1)
    else:
        result_1 = self.find_trap_water(height, 0, height.index(max_height) + 1, 1)
        result_2 = self.find_trap_water(height, len(height) - 1, height.index(max_height) - 1, -1)
        result = result_1 + result_2
    return result


def find_trap_water(self, arr, i_s, i_e, step):
    max_val = -1
    final_res = 0
    out = 0
    for i in range(i_s, i_e, step):
        if arr[i] >= max_val:
            max_val = arr[i]
            final_res += out
            out = 0
        else:
            out += max_val - arr[i]
    return final_res