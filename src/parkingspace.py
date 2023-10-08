class ParkingSpace:
    def __init__(self, start_spot, capacity):
        self.spots = {spot: None for spot in range(start_spot, start_spot + capacity)}

    def assign_spot(self, license_plate_number):
        for spot, occupied in self.spots.items():
            if occupied is None:
                self.spots[spot] = license_plate_number
                return spot
        return None  # No available parking spots

    def retrieve_spot(self, license_plate_number):
        for spot, occupied in self.spots.items():
            if occupied == license_plate_number:
                return spot
        return None  # Vehicle not found
