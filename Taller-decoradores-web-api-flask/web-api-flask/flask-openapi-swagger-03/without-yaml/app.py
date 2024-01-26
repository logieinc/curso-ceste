import flask
from flask_restful import Api
from flasgger import Swagger

app = flask.Flask(__name__)
api = Api(app)
swagger = Swagger(app)

@app.route("/flights")  # GET: Obtener todos los vuelos
def get_flights():
    """
    Nombre y parametros recibidos
    ---
    tags:
      - Flight
    responses:
      200:
        description: OK.
    """
    return {}

@app.route("/flights", methods=["POST"])  # POST: Crear un vuelo
def create_usuario():
    data = flask.request.get_json()
    return {}

@app.route("/flights/<int:id>", methods=["PUT"])  # PUT: Actualizar un vuelo
def update_usuario(id):
    data = flask.request.get_json()
    return {"usuario": data["nombre"]}

@app.route("/flights/<int:id>", methods=["DELETE"])  # DELETE: Eliminar un vuelo
def delete_usuario(id):
    return {"id": id}

if __name__ == "__main__":
    app.run()