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