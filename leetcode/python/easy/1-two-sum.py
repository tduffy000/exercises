class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # given a + b = target
        # dict mapping a required complement to the a index
        
        complements = {} # complement -> index
        for idx, a in enumerate(nums):
            
            # check if this a solves a + b = target
            if a in complements:
                return [complements[a], idx]
            
            b = target - a
            if b not in complements:
                complements[b] = idx
            
        return [-1, -1]
