from flask import render_template

import config

from models import Flight

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")

@app.route("/")
def home():
    flights = Flight.query.all()
    return render_template("home.html", flights=flights)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)