import logging
import os
from logging.handlers import RotatingFileHandler

class Logger:
    """
    Implementação do Logger utilizando o padrão Singleton.
    Garante que exista apenas uma instância do Logger em toda a aplicação.
    Salva logs em arquivo local com rotação automática.
    """
    _instance = None
    
    @classmethod
    def get_instance(cls):
        """
        Método de classe que retorna a instância única do Logger.
        Se a instância não existir, cria uma nova.
        """
        if cls._instance is None:
            cls._instance = Logger()
        return cls._instance
    
    def __init__(self):
        """
        Inicializa o Logger e verifica se já existe uma instância.
        Impede a criação direta de múltiplas instâncias.
        """
        if Logger._instance is not None:
            raise Exception("Esta classe é um Singleton. Use Logger.get_instance() para obter a instância.")
        
        # Diretório onde os logs serão armazenados
        self.log_dir = 'logs'
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        
        # Criação do logger
        self.logger = logging.getLogger('app_logger')
        self.logger.setLevel(logging.INFO)
        
        # Formato para as mensagens de log
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
        
        # Handler para o console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        
        # Handler para arquivo com rotação (1MB por arquivo e máximo de 10 arquivos)
        file_handler = RotatingFileHandler(
            os.path.join(self.log_dir, 'application.log'),
            maxBytes=1024 * 1024,  # 1MB
            backupCount=10
        )
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
    
    def log(self, message, level="INFO"):
        """
        Registra uma mensagem com o nível especificado.
        
        Args:
            message (str): A mensagem a ser registrada
            level (str): O nível do log (INFO, WARNING, ERROR)
        """
        if level == "INFO":
            self.logger.info(message)
        elif level == "WARNING":
            self.logger.warning(message)
        elif level == "ERROR":
            self.logger.error(message)

    def info(self, message):
        """Registra uma mensagem com nível INFO."""
        self.log(message, "INFO")
        
    def warning(self, message):
        """Registra uma mensagem com nível WARNING."""
        self.log(message, "WARNING")
        
    def error(self, message):
        """Registra uma mensagem com nível ERROR."""
        self.log(message, "ERROR")
