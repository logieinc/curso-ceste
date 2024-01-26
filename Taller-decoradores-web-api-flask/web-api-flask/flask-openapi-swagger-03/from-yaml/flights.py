from flask import abort, make_response, request

from models import Flight, flight_schema, flights_schema
from config import db


'''
    Lista de vuelos
'''
def get_flights():
    flights = Flight.query.all()
    return flights_schema.dump(flights)

'''
    Crea vuelo
'''
def create():
# TODO
    pass

'''
    Busqueda vuelo con origen
'''
def read_one(origin):
# TODO
    pass

'''
    Actualizar vuelo
'''
def update(origin):
# TODO
    pass

'''
    Eliminar vuelo
'''
def delete(origin):
# TODO
    pass