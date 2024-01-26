from datetime import datetime

from config import app, db
from models import Flight

FLIGHTS = [
    {
        "origin": "EZE",
        "destination": "POS",
        "departure_date" : "2024-01-25T03:09:10.853Z",
        "arrival_date" : "2024-01-25T03:09:10.853Z",
        "price" : 100.20
    },
    {
        "origin": "COR",
        "destination": "USU",
        "departure_date" : "2024-01-25T03:09:10.853Z",
        "arrival_date" : "2024-01-25T03:09:10.853Z",
        "price" : 400.32
    }
]

with app.app_context():
    db.drop_all()
    db.create_all()
    for data in FLIGHTS:
        new_flight = Flight(origin=data.get("origin"),
                            destination=data.get("destination"),
                            departure_date=datetime.strptime(
                                data.get("departure_date"), "%Y-%m-%dT%H:%M:%S.%fz"
                            ),
                            arrival_date=datetime.strptime(
                                data.get("arrival_date"), "%Y-%m-%dT%H:%M:%S.%fz"
                            ),
                            price = data.get("price"))
        db.session.add(new_flight)
    db.session.commit()
