class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        longest, current = 0, 0
        last = None
        while len(nums) > 0:
            x = nums.pop(0)
            if last is None:
                current += 1
                last = x
                continue
                
            if x <= last:
                longest = max(longest, current)
                current = 1
            else:
                current += 1
            last = x
        longest = max(longest, current)
        return longest
