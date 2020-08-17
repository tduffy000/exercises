class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {ch: i for i, ch in enumerate(order)}
        for i, w in enumerate(words):
            words[i] = [order_map[ch] for ch in w]
        for i in range(len(words)):
            try:
                if words[i] > words[i+1]:
                    return False
            except IndexError:
                break
        return True
