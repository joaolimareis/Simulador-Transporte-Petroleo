import logging

# Configuração do logger
logging.basicConfig(
    filename="simulacao.log",  # Salva os logs em um arquivo
    level=logging.INFO,        # Define o nível de log
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_logger(name):
    """Retorna um logger configurado."""
    return logging.getLogger(name)
