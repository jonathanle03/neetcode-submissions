class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        res = -1

        while right >= left:
            mid = (left + right) // 2

            if nums[mid] == target:
                res = mid
                break
            elif nums[left] == target:
                res = left
                break
            elif nums[right] == target:
                res = right
                break

            if nums[left] < target and nums[mid] < target and nums[right] < target:
                if nums[left] < nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
                continue
            
            if nums[left] > target and nums[mid] > target and nums[right] > target:
                if nums[left] < nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
                continue
            
            if nums[left] < target and nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target and nums[right] > target:
                left = mid + 1
            else:
                break

        return res