# Beats 99% solutions

from collections import deque


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.result_arr = deque()
        self.flatten_list(nestedList)

    def next(self) -> int:
        return self.result_arr.pop()

    def hasNext(self) -> bool:
        return len(self.result_arr)

    def flatten_list(self, arr):
        for i in arr:
            if i.isInteger():
                self.result_arr.appendleft(i.getInteger())
            else:
                self.flatten_list(i.getList())
