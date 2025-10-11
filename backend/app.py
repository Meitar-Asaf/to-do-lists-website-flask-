from flask import Flask, jsonify
from flask_cors import CORS
from seed import run_seed
import os
import redis
from flask-session import Session
from routes import routes


run_seed()
app = Flask(__name__)
CORS(app)

app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_REDIS'] = redis.from_url(os.getenv('REDIS_URL', 'redis://localhost:6379'))
app.confing['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the To-Do List API!"})

if __name__ == "__main__":
    app.register_blueprint(routes, url_prefix="/tasks")
    app.run(host="0.0.0.0", port=5000)


