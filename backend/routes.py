from flask import Blueprint, jsonify

tasks = Blueprint('tasks', __name__)


@tasks.route('/', methods=['GET'])
def get_tasks():
    # דוגמה לראוט שמחזיר רשימת משימות
    return jsonify({'tasks': []})
