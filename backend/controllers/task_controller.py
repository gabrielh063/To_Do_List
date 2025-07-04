from flask import jsonify, request
from database.db import Database
from models.task_model import Task
from logger import Logger

logger = Logger.get_instance()

def get_tasks():
    try:
        query = "SELECT * FROM TASKS"
        results = Database.execute(query)
                                                                                    
        # Cria uma lista de objetos Task
        TASKS = [Task(**task) for task in results]
        
        # Converte cada objeto Task para um dicionário
        tasks_dict = [task.to_dict() for task in TASKS]
        
        logger.info("Tarefas obtidas com sucesso.")
        return jsonify(tasks_dict), 200
    except Exception as e:
        logger.error(f"Falha ao obter tarefas: {e}")
        return jsonify({"error": "Falha ao obter tarefas"}), 500

def get_task_by_id(task_id):
    try:
        query = "SELECT * FROM TASKS WHERE ID_TASK = %s"
        params = (task_id,)
        result = Database.execute(query, params)

        if result and len(result) > 0:
            task = Task(**result[0])
            return jsonify(task.to_dict()), 200
        else:
            return jsonify({"error": "Tarefa não encontrada"}), 404
    except Exception as e:
        print(f"Erro ao buscar tarefa: {e}")
        return jsonify({"error": "Falha ao buscar tarefa"}), 500

def add_task():
    try:
        data = request.get_json()
        query = "INSERT INTO TASKS (TASK_TITLE, TASK_DESC, TASK_IS_DONE) VALUES (%s, %s, %s)"
        params = (data['TASK_TITLE'], data['TASK_DESC'], data['TASK_IS_DONE'])
        Database.execute(query, params)
        
        logger.info(f"Tarefa '{data['TASK_TITLE']}' adicionada com sucesso.")
        return jsonify({"message": "Tarefa adicionada com sucesso"}), 201
    except Exception as e:
        logger.error(f"Falha ao adicionar tarefa: {e}")
        return jsonify({"error": "Falha ao adicionar tarefa"}), 500

def update_task(TASK_ID):
    try:
        data = request.get_json()

        # Cria uma lista de pares de chave-valor a serem atualizados
        fields_to_update = []

        # Verifique se os campos estão presentes e adicione à lista de atualização
        if 'TASK_TITLE' in data:
            fields_to_update.append(f"TASK_TITLE = %s")
        if 'TASK_DESC' in data:
            fields_to_update.append(f"TASK_DESC = %s")
        if 'TASK_IS_DONE' in data:
            fields_to_update.append(f"TASK_IS_DONE = %s")

        if not fields_to_update:
            return jsonify({"error": "Nenhum dado para atualizar"}), 400
        
        # Monta a query dinamicamente
        set_clause = ", ".join(fields_to_update)
        query = f"UPDATE TASKS SET {set_clause} WHERE ID_TASK = %s"
        
        # Organiza os parâmetros para a query
        params = tuple(data[key] for key in data.keys()) + (TASK_ID,)
        
        # Executa a query
        Database.execute(query, params)
        
        return jsonify({"message": "Tarefa atualizada com sucesso"}), 200
    except Exception as e:
        print(f"Erro ao atualizar tarefa: {e}")
        return jsonify({"error": "Falha ao atualizar tarefa"}), 500

def delete_task(ID_TASK):
    try:
        query = "DELETE FROM TASKS WHERE ID_TASK = %s"
        params = (ID_TASK,)
        Database.execute(query, params)
        
        logger.info(f"Tarefa {ID_TASK} removida com sucesso.")
        return jsonify({"message": "Tarefa removida com sucesso"}), 200
    except Exception as e:
        logger.error(f"Falha ao remover tarefa: {e}")
        return jsonify({"error": "Falha ao remover tarefa"}), 500
