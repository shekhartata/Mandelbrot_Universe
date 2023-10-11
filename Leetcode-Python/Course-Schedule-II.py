# Beats 8% solutions, up for improvement

from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not len(prerequisites):
            return list(range(numCourses))
        mapper = defaultdict(list)
        for item in prerequisites:
            mapper[item[0]].append(item[1])
        for item in set(range(numCourses)) ^ set(mapper.keys()):
            mapper[item] = list()
        res = list()
        seen = set()
        being_seen = set()
        def calculate(key):
            seen.add(key)
            if not len(mapper[key]):
                if key not in res:
                    res.append(key)
                    if key in being_seen:
                        being_seen.remove(key)
            for item in mapper[key]:
                if item in being_seen:
                    return list()
                if item not in seen:
                    being_seen.add(key)
                    if calculate(item) == list():
                        return list()
            if key not in res:
                res.append(key)
                if key in being_seen:
                    being_seen.remove(key)
        for k in list(mapper.keys()):
            calculate(k)
        return res if len(res) == numCourses else list()
