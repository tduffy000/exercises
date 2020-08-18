 class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = 0
        for el in A:
            if el % 2 == 0:
                evenSum += el
        
        ans = []
        for qry in queries:
            val, index = qry
            orig = A[index]
            A[index] += val
            if A[index] % 2 == 0:
                if orig % 2 == 0: # have bigger even number
                    evenSum += val
                else: # new even number
                    evenSum += A[index]
            else:
                if orig % 2 == 0: # removed even number
                    evenSum -= orig
            ans.append(evenSum)
        return ans
        
