class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        i = 1
        facts_found = 0
        while i <= n:
            if n % i == 0:
                facts_found += 1
                if facts_found == k:
                    return i
            i += 1
        return -1
