class Solution:
    
    @staticmethod
    def convert_to_numbering(s):
        numbering = []
        seen = {} # {ch | str} -> number
        
        for el in s:
            if el not in seen:
                seen[el] = len(seen)
            numbering.append(seen[el])
        return numbering        
    
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_numbering = self.convert_to_numbering(pattern)
        s_numbering = self.convert_to_numbering(s.split())
        if len(pattern_numbering) != len(s_numbering):
            return False
        
        for pattern_num, s_num in zip(pattern_numbering, s_numbering):
            if pattern_num - s_num != 0:
                return False
        return True
        
