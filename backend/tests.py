import pytest
from flask import Flask, request
from backend.controllers import task_controller as tc

@pytest.fixture
def task_data():
    return {
        "TASK_TITLE": "Test Task",
        "TASK_DESC": "Test Description",
        "TASK_IS_DONE": False
    }

def test_add_task(monkeypatch, task_data):
    def mock_execute(query, params=None):
        return []

    monkeypatch.setattr(tc.db, "execute", mock_execute)
    monkeypatch.setattr(tc.request, "get_json", lambda: task_data)

    response, status = tc.add_task()
    assert status == 201
    assert response.json["message"] == "Tarefa adicionada com sucesso"

def test_get_tasks(monkeypatch):
    mock_result = [
        {
            "ID_TASK": 1,
            "TASK_TITLE": "Test",
            "TASK_DESC": "Desc",
            "TASK_IS_DONE": False
        }
    ]
    monkeypatch.setattr(tc.db, "execute", lambda query, params=None: mock_result)

    response, status = tc.get_tasks()
    assert status == 200
    assert isinstance(response.json, list)
    assert response.json[0]["TASK_TITLE"] == "Test"

def test_get_task_by_id_found(monkeypatch):
    mock_task = [{
        "ID_TASK": 1,
        "TASK_TITLE": "T1",
        "TASK_DESC": "D1",
        "TASK_IS_DONE": False
    }]
    monkeypatch.setattr(tc.db, "execute", lambda query, params=None: mock_task)

    response, status = tc.get_task_by_id(1)
    assert status == 200
    assert response.json["ID_TASK"] == 1

def test_get_task_by_id_not_found(monkeypatch):
    monkeypatch.setattr(tc.db, "execute", lambda query, params=None: [])

    response, status = tc.get_task_by_id(999)
    assert status == 404
    assert response.json["error"] == "Tarefa não encontrada"

def test_update_task(monkeypatch):
    monkeypatch.setattr(tc.db, "execute", lambda query, params=None: [])

    monkeypatch.setattr(tc.request, "get_json", lambda: {
        "TASK_TITLE": "Updated Title",
        "TASK_DESC": "Updated Desc"
    })

    response, status = tc.update_task(1)
    assert status == 200
    assert response.json["message"] == "Tarefa atualizada com sucesso"

def test_delete_task(monkeypatch):
    monkeypatch.setattr(tc.db, "execute", lambda query, params=None: [])

    response, status = tc.delete_task(1)
    assert status == 200
    assert response.json["message"] == "Tarefa removida com sucesso"
