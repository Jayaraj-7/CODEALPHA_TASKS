class BusPassSystem:
    def __init__(self):
        self.bookings = []

    def book_pass(self):
        name = input("Enter Passenger Name: ")
        age = int(input("Enter Age: "))
        route = input("Enter Route: ")

        price = 500

        booking = {
            "Name": name,
            "Age": age,
            "Route": route,
            "Price": price
        }

        self.bookings.append(booking)

        print("\n✅ Bus Pass Booked Successfully")
        print(f"Passenger : {name}")
        print(f"Route     : {route}")
        print(f"Price     : ₹{price}")

    def view_bookings(self):
        print("\n===== ALL BOOKINGS =====")

        if not self.bookings:
            print("No bookings found.")
            return

        for i, booking in enumerate(self.bookings, start=1):
            print(f"\nBooking {i}")
            print(f"Name  : {booking['Name']}")
            print(f"Route : {booking['Route']}")
            print(f"Price : ₹{booking['Price']}")

system = BusPassSystem()

while True:
    print("\n===== CLOUD BUS PASS SYSTEM =====")
    print("1. Book Pass")
    print("2. View Bookings")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        system.book_pass()

    elif choice == "2":
        system.view_bookings()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")