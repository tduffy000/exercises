class IntegerElementCount:
    
    def __init__(self, val: int, count: int):
        self.val = val
        self.count = count
    
    def __lt__(self, other: IntegerElementCount) -> bool:
        return self.count < other.count

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        while len(nums) > 0:
            n = nums.pop()
            freqs[n] = freqs.get(n, 0) + 1
        
        h = []
        for val, count in freqs.items():
            fr = IntegerElementCount(val, count)
            heapq.heappush(h, fr)
        
        return [ fr.val for fr in heapq.nlargest(k, h)]
