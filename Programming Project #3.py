# Define seat types and prices
SEAT_TYPES = {
    "first_class": {"price": 50},
    "emergency": {"price": 0}, # Emergency seats have no extra fee, but have a responsibility prompt
    "regular": {"price": 0}
}

# Initialize seats
seats = {}
seat_count = 0
# First Class (Row 1)
for i in range(5):
    seat_id = f"1{chr(ord('A') + i)}"
    seats[seat_id] = {"status": "empty", "type": "first_class"}
    seat_count += 1
# Emergency Seats (Rows 2 & 3)
for row in range(2, 4):
    for i in range(5):
        seat_id = f"{row}{chr(ord('A') + i)}"
        seats[seat_id] = {"status": "empty", "type": "emergency"}
        seat_count += 1
# Regular Seats (Row 4)
for i in range(5):
    seat_id = f"4{chr(ord('A') + i)}"
    seats[seat_id] = {"status": "empty", "type": "regular"}
    seat_count += 1

# Ensure we have exactly 20 seats
if len(seats) != 20:
    raise Exception("Seat initialization error: incorrect number of seats.")