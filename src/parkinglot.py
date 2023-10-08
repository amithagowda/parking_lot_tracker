from src.settings import INITIAL_FLOORS
from src.parkinglevels import Level
from src.exceptions import DuplicateLicensePlateException, NoAvailableParkingSpotException, VehicleNotFoundException

class ParkingLot:
    def __init__(self):
        self.levels = []
        self.unique_license_plates = set()
        # Default levels A and B with a capacity of 20 each
        
        for floor_settings in INITIAL_FLOORS:
            self.add_level(floor_settings['name'], floor_settings['capacity'])

    def add_level(self, name, capacity):
        if self.levels:
            previous_level = self.levels[-1]
            start_spot = previous_level.start_spot
        else:
            start_spot = 1
        
        level = Level(name, capacity, start_spot)
        self.levels.append(level)

    def is_spot_available(self):
        for level in self.levels:
            if None in level.parking_space.spots.values():
                return True
        raise NoAvailableParkingSpotException("No parking spots available at the moment")

    def assign_parking_spot(self, license_plate_number):
        if license_plate_number in self.unique_license_plates:
            raise DuplicateLicensePlateException("License plate number already in use.")

        for level in self.levels:
            spot = level.parking_space.assign_spot(license_plate_number)
            if spot is not None:
                self.unique_license_plates.add(license_plate_number)
                return {'level': level.name, 'spot': spot}
        raise NoAvailableParkingSpotException("No available parking spots.")

    def retrieve_parking_spot(self, license_plate_number):
        for level in self.levels:
            spot = level.parking_space.retrieve_spot(license_plate_number)
            if spot is not None:
                return {'level': level.name, 'spot': spot}
        raise VehicleNotFoundException("Vehicle not found.")
