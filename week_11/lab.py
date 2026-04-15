print("Exercise 1:\n---------------")
class FlightTicket:
    airline = "Oceanic Airlines"
    airline_code = "OA"

    def __init__(self, flight_num=1, airport="JFK", gate="I1-1", time="8:00", seat="1A",
                 passenger="unknown"):
        self.flight_num = flight_num
        self.airport = airport
        self.gate = gate
        self.time = time
        self.seat = seat
        self.passenger = passenger

    def print_info(self):
        print(f"Airline: {FlightTicket.airline} ({FlightTicket.airline_code})")
        print(f"Flight: {self.flight_num}")
        print(f"Airport: {self.airport}")
        print(f"Gate: {self.gate}")
        print(f"Time: {self.time}")
        print(f"Seat: {self.seat}")
        print(f"Passenger: {self.passenger}")

# Given input
flight_num = 2121
airport = "KEF"
gate = "D22B"
time = "11:45"
seat = "12B"
passenger = "Jules Laurent"

# Output
ticket = FlightTicket(flight_num, airport, gate, time, seat, passenger)
ticket.print_info()

print("\nExercise 2:\n---------------")
class Book:
    imprint = "Fantasy Tomes"

    def __init__(self, title=" ", author=" ", year=0, pages=0):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def print_info(self):
        print(f"{self.title} by {self.author}, published by {Book.imprint}")
        print(f"in {self.year}, with {self.pages} pages")

# Given input for book 1
title1 = "Lord of the Bracelets"
author1 = "Blake R. R. Brown"
year1 = 1999
pages1 = 423

book1 = Book(title1, author1, year1, pages1)

# Given input for book 2
title2 = "A Match of Thrones"
author2 = "Terry R. R. Thomas"
year2 = 2020
pages2 = 761

book2 = Book(title2, author2, year2, pages2)

# Output
book1.print_info()
book2.print_info()

print("\nExercise 3:\n---------------")
class VendingMachine:
    def __init__(self, count=0, max=0):
        self.count = count
        self.max = max

    def refill(self):
        self.count = self.max
        print("Refilled")

    def sell(self, order):
        self.count -= order
        print(f"Sold: {order}")

    def print_stock(self):
        print(f"Current stock: {self.count}")

# Given input
max_value = 100
order = 25

vm = VendingMachine(max_value, max_value)

# Output
vm.print_stock()
vm.sell(order)
vm.print_stock()
vm.refill()
vm.print_stock()

print("\nExercise 4:\n---------------")
class ExerciseLog:
    def __init__(self, e_type="", duration=0):
        self.e_type = e_type
        self.duration = duration

    def __str__(self):
        return f"{self.e_type}: {self.duration} minutes"

    def __add__(self, other):
        if isinstance(other, ExerciseLog):
            # Combine two logs
            return ExerciseLog(f"{self.e_type} & {other.e_type}",
                               self.duration + other.duration)
        elif isinstance(other, int):
            # Add integer to duration
            return ExerciseLog(self.e_type, self.duration + other)
        else:
            return NotImplemented