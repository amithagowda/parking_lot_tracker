class ParkingLotException(Exception):
    """Base class for parking lot exceptions."""


class NoAvailableParkingSpotException(ParkingLotException):
    """Exception raised when there are no available parking spots."""


class VehicleNotFoundException(ParkingLotException):
    """Exception raised when a vehicle is not found in the parking lot."""


class DuplicateLicensePlateException(ParkingLotException):
    """Exception raised when a duplicate license plate number is detected."""
