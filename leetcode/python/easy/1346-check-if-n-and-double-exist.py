class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        found = set()
        complements = set()
        for n in arr:
            if n in complements:
                return True
            found.add(n)
            complements.add(n * 2)
            if n % 2 == 0:
                complements.add(int(n / 2))
        return False
