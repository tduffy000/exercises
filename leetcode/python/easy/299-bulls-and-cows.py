class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        charCounts = {}
        for ch in secret:
            charCounts[ch] = charCounts.get(ch, 0) + 1
        
        bulls, cows = 0, 0
        bullPos = set()
        for idx, (i, j) in enumerate(zip(secret, guess)):
            if i == j:
                if charCounts[i] != 0:
                    bulls += 1
                    charCounts[i] -= 1
                    bullPos.add(idx)
        for idx, i in enumerate(guess):
            if i in charCounts:
                if charCounts[i] != 0 and idx not in bullPos:
                    charCounts[i] -= 1
                    cows += 1
        return f'{bulls}A{cows}B'
