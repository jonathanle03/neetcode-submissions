class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        min_speed = right

        while right >= left:
            mid = (right + left) // 2
            time = 0

            for pile in piles:
                time += math.ceil(pile / mid)
            
            if time <= h:
                min_speed = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return min_speed