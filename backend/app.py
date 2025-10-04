from flask import Flask, jsonify
from flask_cors import CORS
from seed import run_seed

run_seed()
app = Flask(__name__)
CORS(app)
from routes import routes


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the To-Do List API!"})

if __name__ == "__main__":
    app.register_blueprint(routes, url_prefix="/tasks")
    app.run(host="0.0.0.0", port=5000)


