from controllers.task_controller import get_tasks, add_task, update_task, delete_task

task_blueprint = Blueprint('tasks', __name__)

@task_bp.route('/tasks', methods='GET')
    def list_tasks():
        return get_tasks()