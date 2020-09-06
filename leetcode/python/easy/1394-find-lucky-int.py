class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = {}
        for el in arr:
            counts[el] = counts.get(el, 0) + 1
        lucky = -1
        for num, count in counts.items():
            if num == count:
                lucky = max(lucky, num)
        return lucky
