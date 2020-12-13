class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # walk down and if != val, put it back to the beginning
        walker_idx = 0
        for el in nums:
            if el != val:
                nums[walker_idx] = el
                walker_idx += 1
        return walker_idx
