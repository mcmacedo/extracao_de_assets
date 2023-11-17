import os
import sys

from json_files import extrair_arquivos_json
from database import extrair_ativos


def get_env_config(environment):
    if environment in ["DEV", "TEST", "HML"]:
        engine_str = "sqlite:///ativos.db"
        ativos_src = extrair_arquivos_json
    elif environment == "PROD":
        engine_str = os.getenv("DB_ENGINE")
        ativos_src = extrair_ativos

    else:
        raise Exception("A valor de environment não corresponde ao valores esperado: DEV, TEST, HML, PROD")

    return {
        'engine_str': engine_str,
        'ativos_src': ativos_src
    }

def get_argv_config():
    environment = None
    if len(sys.argv) > 1:
        environment = sys.argv[1]
    else:
        raise Exception("É necessário definir o environment. Opções: DEV, TEST, HML, PROD")
    
    return environment