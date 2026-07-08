class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        chars = defaultdict(int)
        char_count = 0
        max_len = 0

        for right in range(len(s)):
            chars[s[right]] += 1
            curr_len = right - left + 1
            char_count = max(chars.values())

            if curr_len > char_count + k:
                chars[s[left]] -= 1
                left += 1
                char_count = max(chars.values())

            max_len = max(max_len, right - left + 1)
        
        return max_len