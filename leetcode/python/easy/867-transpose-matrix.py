class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        rowLength = len(A[0])
        m = []
        for idx in range(rowLength):
            col = [ row[idx] for row in A ]
            m.append(col)
        return m
