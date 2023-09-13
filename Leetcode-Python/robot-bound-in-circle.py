# intuitive check on directions and point beats 89p

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        mapper = {
            'L': [1, -1, -1, 1],
            'R': [1, 1, -1, -1]
        }
        self.l_idx = 0
        self.r_idx = 0
        def calculate(direction, point, multiplier = 1):
            for char in instructions:
                if char == 'L':
                    direction = int(not direction)
                    multiplier = mapper[char][(self.l_idx + 1) % 4]
                    self.l_idx += 1
                    self.r_idx -= 1
                elif char == 'R':
                    direction = int(not direction)
                    multiplier = mapper[char][(self.r_idx + 1) % 4]
                    self.r_idx += 1
                    self.l_idx -= 1
                elif char == 'G':
                    if multiplier:
                        point[direction] += multiplier
                    else:
                        point[direction] += 1
            if point == [0,0] or (direction != 1 or multiplier != 1):
                return True
            return False
        return calculate(1, [0,0])
