class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        nums = [0,0,1]
        for _ in range(n-1):
            nums.append(sum(nums[-3:]))
            nums.pop(0) # discard left-most
        return nums[-1]
            
