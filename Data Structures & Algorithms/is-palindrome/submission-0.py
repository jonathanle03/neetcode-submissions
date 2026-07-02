class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        for i in range(len(text) // 2):
            if text[i] != text[-i - 1]:
                return False
        return True