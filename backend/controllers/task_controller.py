import pymysql
import pymysql.cursors
from dbConfig import connect_db
from flask import jsonify
from flask import flash, request, Blueprint, current_app

task_bp = Blueprint("/task_bp", __name__)

@task_bp.route("/task")
def task():
    try:
        conn = connect_db()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * FROM task")
        rows = cur.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()

@task_bp.route("/task/<id>")
def taskById(id):
    try:
        conn = connect_db()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * FROM task WHERE idTask = %s", (id))
        rows = cur.fetchall()
        resp = jsonify(rows[0])
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
        


@task_bp.route("/task", methods = ["POST"])
def taskPost():
    try:
        conn = connect_db()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        task = request.json
        taskTitle = task["taskTitle"]
        taskDesc = task["taskDesc"]
        taskTipe = task["taskTipe"]
        cur.execute("INSERT INTO task (taskName, taskDesc, taskTipe) VALUES (%s,%s,%s)",(taskTitle, taskDesc, taskTipe))
        conn.commit()
        resp = jsonify({"message": "inserido"})     
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()

@task_bp.route("/task/<id>/", methods = ["PUT"])
def taskPut(id):
    try:
        conn = connect_db()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        task = request.json
        taskTitle = task["taskTitle"]
        taskDesc = task["taskDesc"]
        taskTipe = task["taskTipe"]
        cur.execute("UPDATE task SET taskTitle = %s, taskDesc = %s, taskTipe = %s ",(taskTipe, taskDesc, taskTipe, id))
        conn.commit()
        resp = jsonify({"message": "alterado"})
        rows = cur.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return e
    finally:
        cur.close()
        conn.close()

@task_bp.route("/task/<id>/", methods = ["DELETE"])
def taskDelete(id):
    try:
        conn = connect_db()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("DELETE FROM task WHERE idTask = %s", (id))
        conn.commit()
        resp = jsonify({"message": "excluido"})
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()