class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars = defaultdict(int)
        for c in s1:
            chars[c] += 1
        prev_chars = chars.copy()

        for left in range(len(s2) - len(s1) + 1):
            for i in range(len(s1)):
                chars[s2[left + i]] -= 1
            if min(chars.values()) == 0 and max(chars.values()) == 0:
                return True
            chars = prev_chars.copy()

        return False