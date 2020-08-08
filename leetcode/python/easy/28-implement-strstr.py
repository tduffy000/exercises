class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needleAsList = list(needle)
        if needle == "":
            pos = 0
        else:
            pos = -1
        for i in range(len(haystack)):
            try:
                if list(haystack[i:i+len(needleAsList)]) == needleAsList:
                    pos = i
                    break
            except IndexError:
                break
        return pos
