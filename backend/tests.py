import pytest
import json
from unittest.mock import patch
from app import app
from controllers import task_controller

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

class TestTaskController:
    """Testes para as funções do task_controller.py"""

    @patch('controllers.task_controller.Database.execute')
    def test_get_tasks_success(self, mock_execute):
        mock_execute.return_value = [
            {"ID_TASK": 1, "TASK_TITLE": "Tarefa 1", "TASK_DESC": "Desc 1", "TASK_IS_DONE": False},
            {"ID_TASK": 2, "TASK_TITLE": "Tarefa 2", "TASK_DESC": "Desc 2", "TASK_IS_DONE": True}
        ]
        with app.app_context():
            response, status = task_controller.get_tasks()
            data = json.loads(response.get_data(as_text=True))

            assert status == 200
            assert isinstance(data, list)
            assert data[0]['ID_TASK'] == 1
            assert data[1]['TASK_IS_DONE'] is True

    @patch('controllers.task_controller.Database.execute')
    def test_get_tasks_failure(self, mock_execute):
        mock_execute.side_effect = Exception("DB error")
        with app.app_context():
            response, status = task_controller.get_tasks()
            data = json.loads(response.get_data(as_text=True))

            assert status == 500
            assert "Falha ao obter tarefas" in data['error']

    @patch('controllers.task_controller.Database.execute')
    def test_get_task_by_id_found(self, mock_execute):
        mock_execute.return_value = [
            {"ID_TASK": 1, "TASK_TITLE": "Tarefa 1", "TASK_DESC": "Desc 1", "TASK_IS_DONE": False}
        ]
        with app.app_context():
            response, status = task_controller.get_task_by_id(1)
            data = json.loads(response.get_data(as_text=True))

            assert status == 200
            assert data['ID_TASK'] == 1

    @patch('controllers.task_controller.Database.execute')
    def test_get_task_by_id_not_found(self, mock_execute):
        mock_execute.return_value = []
        with app.app_context():
            response, status = task_controller.get_task_by_id(999)
            data = json.loads(response.get_data(as_text=True))

            assert status == 404
            assert "Tarefa não encontrada" in data['error']

    @patch('controllers.task_controller.Database.execute')
    def test_add_task_success(self, mock_execute):
        mock_execute.return_value = None
        with app.test_request_context(json={
            'TASK_TITLE': 'Nova Tarefa',
            'TASK_DESC': 'Descrição',
            'TASK_IS_DONE': False
        }):
            response, status = task_controller.add_task()
            data = json.loads(response.get_data(as_text=True))

            assert status == 201
            assert "Tarefa adicionada com sucesso" in data['message']

    @patch('controllers.task_controller.Database.execute')
    def test_add_task_failure(self, mock_execute):
        mock_execute.side_effect = Exception("DB insert error")
        with app.test_request_context(json={
            'TASK_TITLE': 'Nova Tarefa',
            'TASK_DESC': 'Descrição',
            'TASK_IS_DONE': False
        }):
            response, status = task_controller.add_task()
            data = json.loads(response.get_data(as_text=True))

            assert status == 500
            assert "Falha ao adicionar tarefa" in data['error']

    @patch('controllers.task_controller.Database.execute')
    def test_update_task_success(self, mock_execute):
        mock_execute.return_value = None
        with app.test_request_context(json={
            'TASK_TITLE': 'Atualizado',
            'TASK_IS_DONE': True
        }):
            response, status = task_controller.update_task(1)
            data = json.loads(response.get_data(as_text=True))

            assert status == 200
            assert "Tarefa atualizada com sucesso" in data['message']

    @patch('controllers.task_controller.Database.execute')
    def test_update_task_no_data(self, mock_execute):
        with app.test_request_context(json={}):
            response, status = task_controller.update_task(1)
            data = json.loads(response.get_data(as_text=True))

            assert status == 400
            assert "Nenhum dado para atualizar" in data['error']

    @patch('controllers.task_controller.Database.execute')
    def test_delete_task_success(self, mock_execute):
        mock_execute.return_value = None
        with app.app_context():
            response, status = task_controller.delete_task(1)
            data = json.loads(response.get_data(as_text=True))

            assert status == 200
            assert "Tarefa removida com sucesso" in data['message']

    @patch('controllers.task_controller.Database.execute')
    def test_delete_task_failure(self, mock_execute):
        mock_execute.side_effect = Exception("DB delete error")
        with app.app_context():
            response, status = task_controller.delete_task(1)
            data = json.loads(response.get_data(as_text=True))

            assert status == 500
            assert "Falha ao remover tarefa" in data['error']

class TestRoutes:
    """Testes para as rotas da aplicação"""

    @patch('controllers.task_controller.Database.execute')
    def test_list_tasks_route(self, mock_execute, client):
        mock_execute.return_value = [
            {"ID_TASK": 1, "TASK_TITLE": "Tarefa 1", "TASK_DESC": "Desc 1", "TASK_IS_DONE": False}
        ]

        response = client.get('/tasks')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        assert data[0]['ID_TASK'] == 1

    @patch('controllers.task_controller.Database.execute')
    def test_get_task_route(self, mock_execute, client):
        mock_execute.return_value = [
            {"ID_TASK": 1, "TASK_TITLE": "Tarefa 1", "TASK_DESC": "Desc 1", "TASK_IS_DONE": False}
        ]

        response = client.get('/tasks/1')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['ID_TASK'] == 1

    @patch('controllers.task_controller.Database.execute')
    def test_add_task_route(self, mock_execute, client):
        mock_execute.return_value = None
        new_task = {
            'TASK_TITLE': 'Nova Tarefa',
            'TASK_DESC': 'Descrição',
            'TASK_IS_DONE': False
        }
        response = client.post('/tasks', json=new_task)
        assert response.status_code == 201
        data = json.loads(response.data)
        assert "Tarefa adicionada com sucesso" in data['message']

    @patch('controllers.task_controller.Database.execute')
    def test_update_task_route(self, mock_execute, client):
        mock_execute.return_value = None
        update_data = {'TASK_TITLE': 'Atualizado', 'TASK_IS_DONE': True}
        response = client.put('/tasks/1', json=update_data)
        assert response.status_code == 200
        data = json.loads(response.data)
        assert "Tarefa atualizada com sucesso" in data['message']

    @patch('controllers.task_controller.Database.execute')
    def test_delete_task_route(self, mock_execute, client):
        mock_execute.return_value = None
        response = client.delete('/tasks/1')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert "Tarefa removida com sucesso" in data['message']
