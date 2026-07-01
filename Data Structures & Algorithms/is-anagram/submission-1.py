class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = dict()
        t_counts = dict()

        for i in s:
            if i in s_counts.keys():
                s_counts[i] += 1
            else:
                s_counts[i] = 1
        
        for i in t:
            if i in t_counts.keys():
                t_counts[i] += 1
            else:
                t_counts[i] = 1
        
        return s_counts == t_counts