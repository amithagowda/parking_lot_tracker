from src.parkingspace import ParkingSpace

class Level:
    def __init__(self, name, capacity, start_spot=1):
        self.name = name
        self.parking_space_capacity = capacity
        self.parking_space = ParkingSpace(start_spot, capacity)
        self.start_spot = start_spot + capacity  #Update the starting spot for the next floor

