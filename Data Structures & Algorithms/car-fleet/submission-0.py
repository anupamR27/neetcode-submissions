class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for car in cars:

            t = (target - car[0]) / car[1]

            if not stack:
                stack.append(t)
            if t > stack[-1]:
                stack.append(t)
            
        return len(stack)