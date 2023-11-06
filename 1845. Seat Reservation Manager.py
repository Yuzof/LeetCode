class SeatManager:
    def __init__(self, n: int):
        self.num_sits = n
        self.seats = [True]*n

    def reserve(self) -> int:
      i = 0
      while i < self.num_sits:
         if self.seats[i] == True:
            self.seats[i] = False
            break
         i += 1
      return i + 1

    def unreserve(self, seatNumber: int) -> None:
      self.seats[seatNumber - 1] = True

"""
class SeatManager:
    def __init__(self, n):
        # Min heap to store all unreserved seats.
        self.available_seats = [i for i in range(1, n + 1)]

    def reserve(self):
        # Get the smallest-numbered unreserved seat from the min heap.
        seat_number = heapq.heappop(self.available_seats)
        return seat_number

    def unreserve(self, seat_number):
        # Push the unreserved seat back into the min heap.
        heapq.heappush(self.available_seats, seat_number)
"""


# Your SeatManager object will be instantiated and called as such:
obj = SeatManager(10)
param_1 = obj.reserve()
print(param_1)
obj.unreserve(1)