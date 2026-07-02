class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spd in sorted_cars:
            time = (target - pos) / spd
            if len(stack) == 0 or time > stack[-1]:
                stack.append(time)
        
        return len(stack)