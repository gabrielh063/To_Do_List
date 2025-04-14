from flask import Flask, send_from_directory
from routes import task_bp
import os

# Corrigindo o caminho relativo da pasta estática
frontend_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '../frontend/static'))

app = Flask(__name__, static_url_path='', static_folder=frontend_folder)
app.register_blueprint(task_bp)

@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
