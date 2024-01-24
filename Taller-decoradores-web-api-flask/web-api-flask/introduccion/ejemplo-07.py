from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app, title="Mi API", description="Un ejemplo simple de API")


@api.route("/hello")
class HelloWorld(Resource):
    def get(self):
        return {"message": "¡Hola, mundo!"}


if __name__ == "__main__":
    app.run(debug=True)