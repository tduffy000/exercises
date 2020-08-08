class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # the brute force version
        arr = sorted(arr)
        diff = -1
        for i in range(len(arr)):
            try:
                newDiff = arr[i+1] - arr[i]
                if diff == -1: # first difference
                    diff = newDiff 
                if diff != newDiff:
                    return False
            except IndexError:
                break
        return True
