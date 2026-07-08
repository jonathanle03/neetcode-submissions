class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_chars = dict(Counter(s1))

        for i in range(len(s2) - len(s1) + 1):
            s2_substr_chars = dict(Counter(s2[i:i + len(s1)]))
            if s1_chars == s2_substr_chars:
                return True

        return False