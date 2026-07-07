class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_len = 0
        unique = []

        while right >= left and right < len(s):
            if s[right] in unique:
                unique.pop(0)
                left += 1
            else:
                unique.append(s[right])
                max_len = max(max_len, len(unique))
                right += 1
        
        return max_len