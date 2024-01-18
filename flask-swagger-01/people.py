from datetime import datetime

from flask import abort, make_response


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


PEOPLE = {
    "Rodriguez": {
        "fname": "Ester",
        "lname": "Rodriguez",
        "timestamp": get_timestamp(),
    },
    "Quiroga": {
        "fname": "Maria",
        "lname": "Quiroga",
        "timestamp": get_timestamp(),
    },
    "Perez": {
        "fname": "Juan",
        "lname": "Perez",
        "timestamp": get_timestamp(),
    },
    "Gonzalez": {
        "fname": "Gonzalo",
        "lname": "Gonzalez",
        "timestamp": get_timestamp(),
    },
}


def read_all():
    return list(PEOPLE.values())


def create(person):
    lname = person.get("lname")
    fname = person.get("fname", "")

    if lname and lname not in PEOPLE:
        PEOPLE[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        return PEOPLE[lname], 201
    else:
        abort(406, f"Persona con apellido {lname} ya existe.")


def read_one(lname):
    if lname in PEOPLE:
        return PEOPLE[lname]
    else:
        abort(404, f"Persona con apellido {lname} no se encuentra.")


def update(lname, person):
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname", PEOPLE[lname]["fname"])
        PEOPLE[lname]["timestamp"] = get_timestamp()
        return PEOPLE[lname]
    else:
        abort(404, f"Persona con apellido {lname} no se encuentra.")


def delete(lname):
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(f"{lname} successfully deleted", 200)
    else:
        abort(404, f"Persona con apellido {lname} no se encuentra.")