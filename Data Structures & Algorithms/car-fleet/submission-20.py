class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = zip(position, speed)
        cars = sorted(cars, reverse = True)
        fleets = []

        for car in cars:
            miles_left = target - car[0]
            arrival_time = miles_left / car[1]
            if not len(fleets):
                fleets.append(arrival_time)
            elif fleets[-1] < arrival_time:
                fleets.append(arrival_time)
            # print(car, fleets, arrival_time)

        return len(fleets)