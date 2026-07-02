class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        
        max_area = 0
        left = 0
        right = len(heights) - 1
        while right > left:
            min_side = min(heights[left], heights[right])
            area = min_side * (right - left)
            max_area = max(max_area, area)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return max_area