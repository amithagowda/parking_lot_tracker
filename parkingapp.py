from src.parkinglot import ParkingLot
from src.exceptions import DuplicateLicensePlateException, NoAvailableParkingSpotException, VehicleNotFoundException


class ParkingApp:
    def __init__(self):
        self.parking_lot = ParkingLot()

    def run(self):
        while True:
            print("Options:")
            print("1. Assign Parking Space")
            print("2. Retrieve Parking Space")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                    try:
                        is_empty = self.parking_lot.is_spot_available()
                        if is_empty:
                            license_plate_number = input("Enter license plate number: ")
                            result = self.parking_lot.assign_parking_spot(license_plate_number)
                            print(f"Assigned parking spot: {result}")
                    except (DuplicateLicensePlateException, NoAvailableParkingSpotException) as e:
                        print(f"Error: {e}")
            elif choice == '2':
                license_plate_number = input("Enter license plate number: ")
                try:
                    result = self.parking_lot.retrieve_parking_spot(license_plate_number)
                    print(f"Retrieved parking spot: {result}")
                except VehicleNotFoundException as e:
                    print(f"Error: {e}")
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")



if __name__ == "__main__":
    parking_app = ParkingApp()
    parking_app.run()




