from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request

from services.service import logic

load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


# @app.route("/process", methods=["POST"])
# def process():
#     name = request.form["name"]
#     summary = logic(name=name)
#     return summary


@app.route("/process", methods=["POST"])
def process():
    try:
        # Get the 'name' from the form data in the POST request
        name = request.form.get("name")
        if not name:
            return jsonify({"error": "Missing 'name' in form data"}), 400

        # Call the service layer with the provided name
        agent_response = logic(name=name)

        # Convert the Pydantic object to a JSON string
        # model_dump_json() is the recommended method in Pydantic V2
        response_json = agent_response.model_dump_json(indent=2)

        # Return the JSON response to the client
        # Flask's jsonify will automatically set the Content-Type header to application/json
        return response_json, 200

    except Exception as e:
        # Handle potential errors and return a clean error message
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


# http://127.0.0.1:5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
