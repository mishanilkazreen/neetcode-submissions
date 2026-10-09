class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for i in range(len(cars)):
            stack.append(cars[i])
            if len(stack) > 1:
                ahead_car_time = (target - stack[-2][0]) / stack[-2][1]
                current_car_time = (target - stack[-1][0]) / stack[-1][1]
                if current_car_time <= ahead_car_time:
                    stack.pop()
        return len(stack)
