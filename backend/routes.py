from flask import Blueprint
from controllers.task_controller import get_tasks, add_task, update_task, delete_task

task_bp = Blueprint('tasks', __name__)

@task_bp.route('/tasks', methods=['GET'])
def list_tasks():
    return get_tasks()

@task_bp.route('/tasks', methods=['POST'])
def new_task():
    return add_task()

@task_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def task_update(task_id):
    return update_task(task_id)

@task_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def remove_task(task_id):
    return delete_task(task_id)
