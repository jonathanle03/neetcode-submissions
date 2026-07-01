class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        sorted_nums = sorted(nums_set)
        sequences = []

        for num in sorted_nums:
            in_seq = False

            for seq in sequences:
                if num - 1 == seq[-1]:
                    seq.append(num)
                    in_seq = True
                    break

            if not in_seq:
                sequences.append([num])
        
        max_len = 0
        for seq in sequences:
            if len(seq) > max_len:
                max_len = len(seq)

        print(sequences)
        
        return max_len