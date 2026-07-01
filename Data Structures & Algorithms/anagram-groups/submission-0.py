class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for string in strs:
            letters = [0] * 26
            for c in string:
                index = ord(c) - ord('a')
                letters[index] += 1
            anagram_dict[tuple(letters)].append(string)
        return list(anagram_dict.values())