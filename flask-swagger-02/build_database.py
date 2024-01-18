from datetime import datetime

from config import app, db
from models import Note, Person

PEOPLE_NOTES = [
    {
        "lname": "Perez",
        "fname": "Jose",
        "notes": [
            ("Me lavo los dientes después de cada comida.", "2022-01-06 17:10:24"),
            (
                "El otro día una amiga dijo, tengo los dientes grandes",
                "2022-03-05 22:17:54",
            ),
            ("¿Pagas por internet?", "2022-03-05 22:18:10"),
        ],
    },
    {
        "lname": "Gonzalez",
        "fname": "Maria",
        "notes": [
            (
                "Lo juro, lo haré mejor este año.",
                "2022-01-01 09:15:03",
            ),
            (
                "¡En realidad! ¡De ahora en adelante sólo buenas obras!",
                "2022-02-06 13:09:21",
            ),
        ],
    },
    {
        "lname": "Rodriguez",
        "fname": "Ester",
        "notes": [
            (
                "¡Tenga en cuenta la tasa de inflación actual!",
                "2022-01-07 22:47:54",
            ),
            ("Necesito un nuevo cepillo de dientes", "2022-04-06 13:03:17"),
        ],
    },
]

with app.app_context():
    db.drop_all()
    db.create_all()
    for data in PEOPLE_NOTES:
        new_person = Person(lname=data.get("lname"), fname=data.get("fname"))
        for content, timestamp in data.get("notes", []):
            new_person.notes.append(
                Note(
                    content=content,
                    timestamp=datetime.strptime(
                        timestamp, "%Y-%m-%d %H:%M:%S"
                    ),
                )
            )
        db.session.add(new_person)
    db.session.commit()
