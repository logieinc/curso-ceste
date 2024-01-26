from datetime import datetime

from config import db, ma

class Flight(db.Model):
    __tablename__ = "flight"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String(32))
    destination = db.Column(db.String(32))
    departure_date = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    arrival_date = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    price = db.Column(db.Numeric(10,2))

    @staticmethod
    def to_json(data):
        new_flight = Flight(origin=data.get("origin"),
                            destination=data.get("destination"),
                            departure_date=datetime.strptime(
                                data.get("departure_date"), "%Y-%m-%dT%H:%M:%S.%fz"
                            ),
                            arrival_date=datetime.strptime(
                                data.get("arrival_date"), "%Y-%m-%dT%H:%M:%S.%fz"
                            ),
                            price=data.get("price"))
        return new_flight

class FlightSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Flight
        load_instance = True
        sqla_session = db.session

flight_schema = FlightSchema()
flights_schema = FlightSchema(many=True)
