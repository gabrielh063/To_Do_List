from backend.database.db import Database as db
from backend.models.task_model import Task

def get_tasks():
     try:
        query = "SELECT * FROM tasks"
        results = db.execute(query)
        
        # Cria uma lista de objetos Task
        tasks = [Task(**task) for task in results]
        
        # Converte cada objeto Task para um dicionário
        tasks_dict = [task.to_dict() for task in tasks]
        
        return jsonify(tasks_dict), 200
    except Exception as e:
        print(e)
        return jsonify({"error": "Falha ao obter tarefas"}), 500

def add_task():
    try:
        data = request.get_json()
        query = "INSERT INTO tasks (TASK_TITLE, TASK_DESC, TASK_IS_DONE) VALUES (%s, %s, %s)"
        params = (data['TASK_TITLE'], data['TASK_DESC'], data['TASK_IS_DONE'])
        db.execute(query, params)
        
        return jsonify({"message": "Tarefa adicionada com sucesso"}), 201
    except Exception as e:
        print(e)
        return jsonify({"error": "Falha ao adicionar tarefa"}), 500

def update_task(task_id):
    try:
        data = request.get_json()
        query = "UPDATE tasks SET TASK_TITLE = %s, TASK_DESC = %s, TASK_IS_DONE = %s WHERE task_id = %s"
        params = (data['TASK_TITLE'], data['TASK_DESC'], data['TASK_IS_DONE'], task_id)
        db.execute(query, params)
        
        return jsonify({"message": "Tarefa atualizada com sucesso"}), 200
    except Exception as e:
        print(e)
        return jsonify({"error": "Falha ao atualizar tarefa"}), 500

def delete_task(task_id):
    try:
        query = "DELETE FROM tasks WHERE task_id = %s"
        params = (task_id,)
        db.execute(query, params)
        
        return jsonify({"message": "Tarefa removida com sucesso"}), 200
    except Exception as e:
        print(e)
        return jsonify({"error": "Falha ao remover tarefa"}), 500
