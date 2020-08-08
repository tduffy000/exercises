mapping = {
    'a': 2,
    'b': 1,
    'c': 1,
    'd': 2,
    'e': 3,
    'f': 2,
    'g': 2,
    'h': 2,
    'i': 3,
    'j': 2,
    'k': 2,
    'l': 2,
    'm': 1,
    'n': 1,
    'o': 3,
    'p': 3,
    'q': 3,
    'r': 3,
    's': 2,
    't': 3,
    'u': 3,
    'v': 1,
    'w': 3,
    'x': 1,
    'y': 3,
    'z': 1
}

class Solution(object):
    
    
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        out = []
        while len(words) > 0:
            rowNum = -1
            toAdd = True
            w = words.pop()
            for ch in w:
                thisRowNum = mapping[ch.lower()]
                if thisRowNum != rowNum and rowNum != -1:
                    toAdd = False
                    break
                if rowNum == -1:
                    rowNum = thisRowNum
            if toAdd:
                out.append(w)
        return out
