class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums)):
            j = i + 1
            k = len(sorted_nums) - 1;

            while k > j:
                sum = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]
                if sum > 0:
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    result.add((sorted_nums[i], sorted_nums[j], sorted_nums[k]))
                    j += 1
        
        res_list_tup = list(result)
        res_list_list = [list(tup) for tup in res_list_tup]

        return res_list_list