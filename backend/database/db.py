import pymysql

# Variável para armazenar a conexão
_connection = None

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_NAME = 'TO_DO_LIST'

class Database:
    @staticmethod
    def connect_db():
        global _connection
        try:
            # Verifica se a conexão já existe e está ativa
            if _connection and _connection.open:
                return _connection
            else:
                # Cria uma nova conexão
                _connection = pymysql.connect(
                    host=DB_HOST,
                    user=DB_USER,
                    password=DB_PASSWORD,
                    database=DB_NAME
                )
                return _connection
        except pymysql.MySQLError as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None

    @staticmethod
    def execute(query, params=None):
        conn = Database.connect_db()
        try:
            cur = conn.cursor(pymysql.cursors.DictCursor)
            if params is None:
                cur.execute(query)
            else:
                cur.execute(query, params)

            conn.commit()

            result = cur.fetchall()
            cur.close()
            return result
        except pymysql.MySQLError as e:
            print(f"Falha ao executar a query: {e}")
            conn.rollback()
            return None
        finally:
            pass
