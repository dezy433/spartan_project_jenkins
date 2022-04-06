from flask import Flask, request
import management

app = Flask(__name__)


@app.route("/", methods=["GET"])
def homepage():
    welcome = "Welcome to the Devops Server\n"
    tutorial = (
        "\nAPI is an interface that allows your application to interact with an external service using a simple set of commands.\n You do not need to know the internal logic of the service, just send a simple command and the service will return the necessary data.")
    description = (welcome + "\n" + tutorial)

    return description


@app.route("/spartan/add", methods=["POST"])
def spartan_add():
    result = management.add_to_db()
    return f"{result}"


@app.route("/spartan/<spartan_id>", methods=["GET"])
def spartan_getter(spartan_id):
    data = management.spartan_info(spartan_id)
    return data


@app.route("/spartan", methods=["GET"])
def list_spartans():
    spartans_db = management.display_db()
    return f"{spartans_db}"


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")

