import json
import random
from datetime import datetime, timedelta
import pandas as pd

# Set random seed for reproducibility
random.seed(42)

# Config
NUM_BUSES = 20
NUM_ROUTES = 5
NUM_PASSENGERS = 100
NUM_TRIPS = 200
NUM_PAYMENTS = 500
NUM_EVENTS = 150

start_date = datetime(2026, 8, 20, 6, 0, 0)

# 1. buses.csv
buses = []
for i in range(1, NUM_BUSES + 1):
    buses.append(
        {
            "bus_id": f"B{100 + i}",
            "plate_num": f"MH-12-AB-{1000 + i}",
            "capacity": random.choice([40, 55, 60]),
            "status": random.choice(["Active", "Active", "Active", "Maintenance"]),
        }
    )
df_buses = pd.DataFrame(buses)
df_buses.to_csv("buses.csv", index=False)

# 2. routes.csv
routes = [
    {
        "route_id": "R1",
        "route_name": "Downtown Express",
        "origin": "Central Station",
        "destination": "Tech Park",
        "base_fare": 25.0,
    },
    {
        "route_id": "R2",
        "route_name": "Airport Line",
        "origin": "Central Station",
        "destination": "Airport Terminal 2",
        "base_fare": 50.0,
    },
    {
        "route_id": "R3",
        "route_name": "Suburban Loop",
        "origin": "North Hub",
        "destination": "South Mall",
        "base_fare": 15.0,
    },
    {
        "route_id": "R4",
        "route_name": "University Shuttle",
        "origin": "Metro West",
        "destination": "Campus Gate",
        "base_fare": 10.0,
    },
    {
        "route_id": "R5",
        "route_name": "Harbor Connect",
        "origin": "East Port",
        "destination": "Downtown Express",
        "base_fare": 30.0,
    },
]
df_routes = pd.DataFrame(routes)
df_routes.to_csv("routes.csv", index=False)

# 3. passengers.csv
passengers = []
card_types = ["Standard", "Student", "Senior", "Pass"]
for i in range(1, NUM_PASSENGERS + 1):
    passengers.append(
        {
            "passenger_id": f"P{1000 + i}",
            "full_name": f"Passenger_{i}",
            "card_type": random.choice(card_types),
            "created_at": (
                start_date - timedelta(days=random.randint(10, 100))
            ).strftime("%Y-%m-%d"),
        }
    )
df_passengers = pd.DataFrame(passengers)
df_passengers.to_csv("passengers.csv", index=False)

# 4. trips.csv (Day 1 batch)
trips = []
for i in range(1, NUM_TRIPS + 1):
    trip_start = start_date + timedelta(
        minutes=random.randint(0, 720)
    )  # within 12 hours
    duration = random.randint(20, 90)
    trip_end = trip_start + timedelta(minutes=duration)
    trips.append(
        {
            "trip_id": f"T{5000 + i}",
            "bus_id": f"B{100 + random.randint(1, NUM_BUSES)}",
            "route_id": f"R{random.randint(1, NUM_ROUTES)}",
            "driver_id": f"D{random.randint(1, 10)}",
            "start_time": trip_start.strftime("%Y-%m-%d %H:%M:%S"),
            "end_time": trip_end.strftime("%Y-%m-%d %H:%M:%S"),
            "passenger_count": random.randint(5, 55),
        }
    )
df_trips = pd.DataFrame(trips)
df_trips.to_csv("trips_01.csv", index=False)

# 5. payments.csv
payments = []
methods = ["SmartCard", "MobileApp", "Cash", "ContactlessCredit"]
for i in range(1, NUM_PAYMENTS + 1):
    p_time = start_date + timedelta(minutes=random.randint(0, 720))
    payments.append(
        {
            "payment_id": f"PAY{10000 + i}",
            "trip_id": f"T{5000 + random.randint(1, NUM_TRIPS)}",
            "passenger_id": f"P{1000 + random.randint(1, NUM_PASSENGERS)}",
            "amount": float(random.choice([10, 15, 25, 30, 50])),
            "payment_method": random.choice(methods),
            "payment_timestamp": p_time.strftime("%Y-%m-%d %H:%M:%S"),
        }
    )
df_payments = pd.DataFrame(payments)
df_payments.to_csv("payments.csv", index=False)

# 6. vehicle_events.json
event_types = [
    "DOOR_OPEN",
    "DOOR_CLOSE",
    "SPEED_WARNING",
    "ENGINE_OVERHEAT",
    "EMERGENCY_BRAKE",
]
events = []
for i in range(1, NUM_EVENTS + 1):
    e_time = start_date + timedelta(minutes=random.randint(0, 720))
    events.append(
        {
            "event_id": f"EVT{8000 + i}",
            "bus_id": f"B{100 + random.randint(1, NUM_BUSES)}",
            "event_type": random.choice(event_types),
            "severity": random.choice(["INFO", "WARNING", "CRITICAL"]),
            "timestamp": e_time.strftime("%Y-%m-%d %H:%M:%S"),
        }
    )

with open("vehicle_events.json", "w") as f:
    json.dump(events, f, indent=2)

print("All 6 synthetic datasets generated successfully!")