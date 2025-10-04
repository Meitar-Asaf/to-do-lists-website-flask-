from flask import Blueprint, jsonify

from src.models.all_models import TodoList, Task
from src.bll.todo_list_facade import TodoListFacade
from src.bll.task_facade import TaskFacade

todo_list_facade = TodoListFacade()
task_facade = TaskFacade()

routes = Blueprint('routes', __name__)

@routes.route('/todo-lists', methods=['GET'])
def get_all_todo_lists():
    todo_lists = todo_list_facade.get_all_todo_lists()
    return jsonify([{
        'id': todo_list.id,
        'name': todo_list.name,
        'user_id': todo_list.user_id
    } for todo_list in todo_lists]), 200
@routes.route('/todo-lists/<int:todo_list_id>/tasks', methods=['GET'])
def get_tasks_by_todo_list(todo_list_id):
    tasks = todo_list_facade.get_tasks_by_todo_list(todo_list_id)
    if tasks is None:
        return jsonify({'message': 'Todo list not found or has no tasks'}), 404
    return jsonify([{
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'todo_list_id': task.todo_list_id
    } for task in tasks]), 200
@routes.route('/tasks', methods=['GET'])
def get_all_tasks():
    tasks = task_facade.get_all_tasks()
    return jsonify([{
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'todo_list_id': task.todo_list_id
    } for task in tasks]), 200
@routes.route('/tasks/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    task = task_facade.get_task_by_id(task_id)
    if task is None:
        return jsonify({'message': 'Task not found'}), 404
    return jsonify({
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'todo_list_id': task.todo_list_id
    }), 200
@routes.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    success = task_facade.delete_task(task_id)
    if success:
        return jsonify({'message': 'Task deleted successfully'}), 200
    return jsonify({'message': 'Task not found'}), 404
