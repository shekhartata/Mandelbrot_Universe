# Using recursive dfs, beats 99p or solutions

class Solution:
    def decodeString(self, s: str) -> str:
        self.res = ""
        self.last_idx = None
        def calculate(idx, string, multiplier=None):
            if idx >= len(s):
                self.res = string
                return
            if s[idx] == "]":
                self.last_idx = idx
                return string
            if s[idx].isdigit():
                if multiplier:
                    multiplier = int(str(multiplier) + s[idx])
                else:
                    multiplier = int(s[idx])
                return calculate(idx + 1, string, multiplier)
            elif s[idx] == "[":
                string += multiplier * calculate(idx + 1, "", None)
                self.res = string
            elif s[idx].isalpha():
                return calculate(idx + 1, string + s[idx])
            if self.last_idx < len(s) - 1:
                return calculate(self.last_idx + 1, string)
        calculate(0, "")
        return self.res
