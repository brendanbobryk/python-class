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