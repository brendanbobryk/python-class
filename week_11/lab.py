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