class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        min_num = 0

        while right >= left:
            mid = (left + right) // 2
            left_val = nums[left]
            mid_val = nums[mid]
            right_val = nums[right]

            if left_val <= right_val:
                min_num = left_val
                break

            if left_val <= mid_val:
                left = mid + 1
            else:
                right = mid
        
        return min_num